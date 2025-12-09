# UToE – Neural Falsification Study

This repository contains the paper, code, and reproducibility materials for an adversarial empirical test of multiplicative versus additive neural dynamics in resting-state fMRI.

The central question is structural:

> When modelling neural signal change as a function of external drive (λ) and internal coherence (γ), is a multiplicative interaction term λ·γ structurally necessary, or are simpler additive drift models sufficient?

No universality is assumed. The study is restricted to the OpenNeuro ds003521 dataset and to predefined cortical networks.

---

## Contents

- `paper.md`  
  Full manuscript for the study, from abstract through conclusion.

- `run_adversarial_test.py`  
  Unified analysis script implementing models M1–M12, model comparison, and the final composite results across subjects and networks.

- `environment.yml`  
  Conda environment specification listing all required Python packages (NumPy, SciPy, Nilearn, Nibabel, etc.).

- `LICENSE`  
  MIT license for code and text in this repository.

- `CITATION.cff`  
  Machine-readable citation metadata.

---

## Summary of the Study

- **Data**  
  Resting-state fMRI from 8 healthy participants (OpenNeuro ds003521), parcellated into 7 Yeo–Schaefer functional networks.

- **Models**  
  - Additive drift model: rate ∝ λ + γ  
  - Multiplicative model: rate ∝ λ·γ  
  along with nested control models and a phase-randomized null.

- **Primary test**  
  Compare multiplicative model (M6) vs additive drift (M7) using ΔAIC and Δ adjusted R², per network and subject.

- **Key result**  
  - Sensory networks (Visual, SomatoMotor): additive drift is sufficient.  
  - Associative networks (Limbic, Ventral Attention, Control, DMN): multiplicative structure is statistically necessary and robust to phase randomization.

The conclusion is a **structural constraint**: the λ·γ product is not universal across cortex but is required in specific high-integration regimes.

---

## How to Reproduce the Analysis

1. **Create environment**

   ```bash
   conda env create -f environment.yml
   conda activate utoe-neural
