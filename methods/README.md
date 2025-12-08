# Methods Overview

This directory defines the empirical methodology used to test bounded
logistic–scalar integration dynamics in genetic and DNA-level systems.

The goal is to determine whether cumulative genetic information
(e.g., expression, regulatory load, evolutionary accumulation)
exhibits bounded, monotonic integration consistent with logistic growth,
rather than unbounded or linear accumulation.

## Core Hypothesis

Genetic systems evolve under structural constraints such that integrated
genomic or expression-level quantities follow bounded logistic dynamics
with saturation, rather than indefinite growth.

## Model Class

The primary model tested is:

dΦ/dt = r · Φ · (1 − Φ / Φ_max)

where Φ represents cumulative genetic integration.

Competing models:
- Linear accumulation
- Exponential growth
- Piecewise drift models

## Validation Criteria

Models are compared using:
- Adjusted R²
- AIC / BIC
- Out-of-sample predictive accuracy

## Domains Covered

- Gene expression time series
- Developmental genomics
- Evolutionary accumulation proxies

This directory defines methodology only.
Implementation lives in `/analysis`.
