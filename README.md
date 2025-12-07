# UToE Neural Falsification Study

This repository contains the complete reproducibility package for the adversarial neural test of the UToE 2.1 logistic–scalar framework.

## Purpose
To test whether neural integration dynamics are better explained by a multiplicative interaction between external drive (λ) and internal coherence (γ), versus canonical additive drift models.

## Contents
- `run_adversarial_test.py` — Full execution pipeline (data loading, γ-parallelization, M1–M12 models, aggregation)
- `environment.yml` — Exact Python environment for reproducibility

## Data
The analysis uses fMRIPrep derivatives from OpenNeuro dataset **ds003521**.

Due to file size constraints, raw neuroimaging data is not included here.

## Status
✅ Pre-registered design  
✅ Adversarial testing  
✅ Phase-randomized null controls  
✅ Network-level aggregation  

## Author
Majid Shabani
