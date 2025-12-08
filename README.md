# UToE – Neural Falsification Study

This repository contains the data pipeline, analysis code, and manuscript for an adversarial empirical test of multiplicative versus additive models of neural dynamics using fMRI data.

The study is explicitly **falsification-driven**. It does not assume that multiplicative (λ·γ) structure holds universally across the brain. Instead, it tests whether such structure is *necessary*, *redundant*, or *invalid* across distinct functional networks.

---

## Core Question

Does a multiplicative interaction between external drive (λ) and internal coherence (γ) provide a statistically superior explanation of neural integration dynamics compared to additive or null alternatives?

---

## Experimental Design

- Dataset: OpenNeuro ds003521 (fMRI, movie-watching task)
- Parcellation: Schaefer 400, 7-network Yeo mapping
- Models tested: M1–M12 (constant, additive, multiplicative, null, phase-randomized controls)
- Evaluation metrics:
  - Out-of-sample adjusted R²
  - AIC / ΔAIC
  - Phase-randomized null comparison

The analysis is preregistered in structure: explicit failure criteria are defined *before* model comparison.

---

## Falsification Criteria

The multiplicative model is considered **falsified** in a network if:

- ΔAdj R² ≤ 0.01 **and**
- ΔAIC ≥ −5

These criteria ensure that small numerical improvements are not misinterpreted as structural necessity.

---

## Summary of Results

- **Sensory and motor networks** (Visual, Somatomotor):  
  Additive models are sufficient; multiplicative structure provides no meaningful advantage.

- **Associative networks** (Default Mode, Control, Ventral Attention):  
  Multiplicative models significantly outperform additive and phase-randomized controls.

- **Null controls** eliminate the effect when temporal coherence is destroyed, confirming phase dependence.

This result **constrains**, rather than universalizes, multiplicative neural dynamics.

---

## Contents

- `paper.md` — Full manuscript with theory, methods, results, and limitations
- `run_adversarial_test.py` — Complete analysis pipeline
- `environment.yml` — Fully reproducible environment
- `CITATION.cff` — Citation metadata

---

## Interpretation

The study demonstrates that multiplicative neural dynamics are **not universal**, but **structurally necessary** in high-level integrative networks. This is the strongest defensible outcome of a falsification-based approach.

---

## License

MIT License
