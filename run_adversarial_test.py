# UToE Neural Falsification — Full Adversarial Test
# Author: M. Shabani
# License: MIT
# Description:
#   This script implements the adversarial neural test comparing
#   multiplicative (λ · γ) dynamics against additive drift models
#   using fMRI-derived time series.

import numpy as np
import pandas as pd
from scipy.signal import savgol_filter
from joblib import Parallel, delayed
import statsmodels.api as sm
from sklearn.metrics import r2_score

# -------------------------------
# Fixed Parameters (Pre-Registered)
# -------------------------------
TR = 2.0
WINDOW_SIZE_GAMMA = 15
SMOOTH_WINDOW_PHI = 11
SMOOTH_POLY_ORDER = 2
EPSILON = 1e-6


# -------------------------------
# Core Variable Construction
# -------------------------------
def construct_phi_and_r(signal):
    magnitude = np.abs(signal)
    phi = np.cumsum(magnitude * TR)
    phi /= np.max(phi)

    w = min(SMOOTH_WINDOW_PHI, len(phi) - 1)
    if w % 2 == 0:
        w -= 1

    phi = savgol_filter(phi, w, SMOOTH_POLY_ORDER)

    r = (np.log(phi[1:] + EPSILON) - np.log(phi[:-1] + EPSILON)) / TR
    valid = phi[:-1] > 0.1 * np.median(phi[:-1])
    return r[valid]


def compute_gamma_window(data, t0):
    window = data[:, t0:t0 + WINDOW_SIZE_GAMMA]
    corr = np.corrcoef(window)
    iu = np.triu_indices_from(corr, k=1)
    return np.mean(corr[iu])


def construct_gamma(data):
    T = data.shape[1]
    gamma_vals = Parallel(n_jobs=-1)(
        delayed(compute_gamma_window)(data, t)
        for t in range(T - WINDOW_SIZE_GAMMA)
    )
    gamma = np.array(gamma_vals)
    gamma = (gamma - gamma.mean()) / gamma.std()
    return gamma


def phase_randomize(x):
    f = np.fft.rfft(x)
    mag = np.abs(f)
    phase = np.random.uniform(0, 2*np.pi, len(f))
    f_null = mag * np.exp(1j * phase)
    y = np.fft.irfft(f_null, n=len(x))
    return (y - y.mean()) / y.std()


# -------------------------------
# Model Fitting
# -------------------------------
def fit_models(R, lam, gam):
    P = lam * gam
    V = lam + gam
    gam_null = phase_randomize(gam)
    Pn = lam * gam_null

    models = {
        "M6_product": np.column_stack([lam, gam, P]),
        "M7_drift": np.column_stack([V]),
        "M11_null_product": np.column_stack([Pn])
    }

    results = {}
    split = int(0.7 * len(R))

    for name, X in models.items():
        X_train = sm.add_constant(X[:split])
        y_train = R[:split]
        X_test = sm.add_constant(X[split:])
        y_test = R[split:]

        try:
            m = sm.OLS(y_train, X_train).fit()
            y_pred = m.predict(X_test)
            adj_r2 = 1 - (1 - r2_score(y_test, y_pred)) * (len(y_test)-1)/(len(y_test)-X_train.shape[1]-1)
            results[name] = {"AIC": m.aic, "Adj_R2": adj_r2}
        except Exception:
            results[name] = {"AIC": np.nan, "Adj_R2": np.nan}

    return results


if __name__ == "__main__":
    print("UToE Neural Adversarial Test — Code Archive Ready")
