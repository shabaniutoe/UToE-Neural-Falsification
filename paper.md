# A Constrained Test of Multiplicative Neural Integration Dynamics  
## An Adversarial fMRI Evaluation of Product vs. Additive Rate Models

**Author:** Majid Shabani  
**Affiliation:** Independent Researcher  
**Date:** December 2025  

---

## Abstract

The dynamical laws governing large-scale neural integration remain an open problem in systems neuroscience. Canonical models typically assume additive contributions of external inputs and internal neural states to the rate of activity accumulation. An alternative class of models proposes that, under certain conditions, integration dynamics are multiplicatively modulated by internal coherence states. This hypothesis makes a strong structural prediction and therefore requires explicit falsification.

Here, we present a pre-registered adversarial comparison between additive drift models and a multiplicative interaction model applied to human fMRI data collected during continuous naturalistic stimulation. The dependent variable is defined as the temporal log-derivative of a cumulatively integrated BOLD magnitude signal, isolating modulation of integration rate rather than signal amplitude. External stimulus drive and internal coherence are operationalized independently and entered into a unified regression framework.

Across eight subjects and 400 cortical parcels, results demonstrate that additive models are sufficient for primary sensory and motor networks, while associative networks—including Default Mode, Control, and Ventral Attention systems—exhibit a reproducible advantage for multiplicative interaction terms. Phase-randomized control analyses confirm that this advantage depends on preserved temporal alignment rather than shared spectral structure.

These findings falsify claims of universal multiplicative integration while identifying a constrained functional regime in which such dynamics provide explanatory value. The work illustrates a falsification-driven approach to evaluating structural dynamical hypotheses in large-scale neural data.

---

## 1. Introduction

Understanding how neural systems integrate activity over time is a central goal of computational neuroscience. Classical approaches model neural activity as the result of additive accumulation processes, whether in the form of firing-rate equations, neural mass models, or drift-diffusion frameworks for decision-making. In these formulations, external inputs and internal states contribute linearly to the rate of change of activity or evidence.

Despite their success, additive models implicitly assume that internal neural coherence functions as a baseline or offset rather than as a gating or modulatory mechanism. Recent theoretical work across neuroscience and complex systems has suggested that, in highly integrated regimes, internal state coherence may instead modulate the influence of external input in a multiplicative manner. Such proposals are attractive but risky: multiplicative models are more complex, less identifiable, and prone to overfitting without careful controls.

For this reason, strong claims of multiplicative integration must be subjected to adversarial testing against simpler canonical alternatives. The present study adopts this strategy explicitly. Rather than attempting to maximize explanatory power, the analysis is designed to invalidate the multiplicative hypothesis wherever additive dynamics are sufficient.

---

## 2. Conceptual Framework

### 2.1 Integrated Neural Signal

For each cortical parcel, we define an integrated activity signal Φ(t) constructed as the cumulative sum of the absolute BOLD signal:

Φ(t) = Σ |X(t)| · Δt

where X(t) is the parcel-wise BOLD signal after nuisance regression and normalization. This quantity represents cumulative activity magnitude rather than instantaneous amplitude.

### 2.2 Log-Rate of Integration

The primary dependent variable is the discrete-time log-rate of Φ(t):

R(t) = [log(Φ(t) + ε) − log(Φ(t − 1) + ε)] / Δt

This transformation isolates changes in integration speed while reducing sensitivity to monotonic growth and scaling differences across parcels.

### 2.3 External and Internal Drivers

Two drivers of integration rate are defined:

- **External driver λ(t):** a hemodynamically convolved stimulus time course derived from task events.
- **Internal driver γ(t):** a time-resolved measure of global functional coherence, computed as the mean off-diagonal correlation across parcels within a sliding temporal window.

These signals are constructed independently and normalized prior to model fitting.

---

## 3. Competing Dynamical Models

All models are evaluated within the same regression framework, differing only in how λ(t) and γ(t) enter the rate equation.

### 3.1 Additive Models

The additive baseline assumes linear contributions:

R(t) = β₀ + βλ·λ(t) + βγ·γ(t) + ε(t)

A simplified drift formulation assumes that only the summed driver matters:

R(t) = β₀ + βv·[λ(t) + γ(t)] + ε(t)

These models correspond closely to firing-rate and drift-diffusion assumptions.

### 3.2 Multiplicative Interaction Model

The multiplicative hypothesis introduces an explicit interaction term:

R(t) = β₀ + βλ·λ(t) + βγ·γ(t) + βp·[λ(t)γ(t)] + ε(t)

The interaction coefficient βp encodes the core structural claim: that internal coherence modulates how external input translates into integration rate.

### 3.3 Phase-Randomized Controls

To test whether any observed advantage depends on temporal alignment, phase-randomized surrogates of γ(t) are generated. These preserve the power spectrum while destroying temporal structure, serving as null controls for interaction effects.

---

## 4. Pre-Registered Falsification Criteria

The multiplicative hypothesis is considered unsupported if, relative to the canonical drift model:

- ΔAIC ≥ −5, and  
- ΔAdjusted R² ≤ 0.01  

across a majority of parcels within a given network.

These thresholds were fixed prior to analysis to prevent post hoc reinterpretation.

---

## 5. Data and Methods

### 5.1 Dataset and Preprocessing

Data were drawn from OpenNeuro dataset ds003521, consisting of fMRI recordings during continuous naturalistic movie viewing. Preprocessed derivatives were obtained using fMRIPrep. Nuisance regression included motion parameters, white matter and CSF signals, global signal, and linear temporal drift.

### 5.2 Parcellation and Subjects

The cortex was parcellated using the Schaefer 400-region atlas with a 7-network functional taxonomy. Eight subjects meeting motion and data completeness criteria were included.

### 5.3 Model Fitting and Validation

For each parcel, models were fit using ordinary least squares. Time series were split chronologically into training (70%) and testing (30%) segments. Model comparison metrics were computed exclusively on held-out data. Parcel-level results were aggregated at the network level.

---

## 6. Results

### 6.1 Additive Sufficiency in Primary Networks

Visual and somatomotor networks consistently satisfied the falsification criteria. Additive drift models explained integration dynamics without requiring interaction terms. Multiplicative coefficients were small and unstable in these systems.

### 6.2 Multiplicative Advantage in Associative Networks

Default Mode, Control, and Ventral Attention networks exhibited reliable improvements in both adjusted R² and AIC when the multiplicative term was included. These effects were consistent across subjects and survived aggregation.

### 6.3 Phase Randomization Analysis

When γ(t) was phase-randomized, the advantage of the multiplicative model collapsed, confirming that observed effects depend on preserved temporal structure rather than shared variance.

---

## 7. Interpretation

The results reject a universal multiplicative law of neural integration while falsifying the claim that additive dynamics are always sufficient. Instead, multiplicative modulation appears selectively in networks associated with internal integration and high-level cognition.

---

## 8. Limitations

This analysis does not establish causality and is limited to BOLD fMRI and one operationalization of coherence. Extension to electrophysiological data and mechanistic models remains necessary.

---

## 9. Conclusion

This work demonstrates the value of adversarial model testing for evaluating structural hypotheses in neuroscience. Multiplicative integration dynamics are not universal but are structurally relevant in specific associative regimes.

---

## 10. Reproducibility Statement

All analysis code, environment specifications, and scripts are publicly available in this repository.

---

## License

MIT License.
