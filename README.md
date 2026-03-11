# The Jinx's Theorem: Main Python Scripts

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18263783.svg)](https://doi.org/10.5281/zenodo.18263783)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Paper](https://img.shields.io/badge/Paper-Zenodo%2FCERN-blue)](https://doi.org/10.5281/zenodo.18930421)

Official repository for:

- *The Jinx's Theorem: Spectral Fingerprinting of Arithmetic Structures Through Quantum Resonance* — Xavier J. Régent (2026)
- *From Undecidability to Cryptographic Efficiency: A Spectral Bridge from the Nitescence Theorem to Arithmetic Structure and Sieve Acceleration* — Xavier J. Régent (2026, in preparation)

---

### Overview

This repository implements the Jinx's Theorem, demonstrating that arithmetic structures possess intrinsic, measurable spectral signatures. By shifting from enumerative complexity to spectral resonance, it provides a new framework for analyzing prime numbers, perfect powers, composite integers, B-smooth numbers, and sieve acceleration.

**Key Features:**
- Square Scan: Spectral signature of perfect squares (20-Qubit resolution).
- Millionaire Scan: Analysis of 82,000+ primes at 2^20 resolution.
- Riemann Alignment: Verification against the first 30 non-trivial zeros.
- Structural Triangulation: Real-time diagnostic of 70+ digit integers.
- **NEW** — B-Smooth Spectral Analysis: Spectral decay signatures of B-smooth numbers via the Dickman polytope framework.
- **NEW** — Spectral Sieve Pre-filtering (SSP): Jinx-accelerated quadratic sieve with empirical gain G > 1 proven.

---

### Quick Start
```bash
pip install numpy matplotlib qiskit qiskit-aer sympy
```

---

### Scripts

____________________________________________________________________________
**1. Universal Scaling Law :: Square Field (Figure 1)**
```bash
python jinx_square.py
```
Evidence of the fundamental k^-1/2 harmonic signature (20-Qubit).

____________________________________________________________________________
**2. Riemann Resonance Alignment (Figure 2)**
```bash
python riemann.py
```
Visual correlation between Jinx peaks and the first 30 Zeta zeros.

____________________________________________________________________________
**3. The Millionaire Scan :: Prime Field (Figure 3)**
```bash
python millionaire_scan.py
```
High-resolution analysis of 82,000+ primes at 2^20 states.

____________________________________________________________________________
**4. Composite Triangulation :: Diagnostic Device (Figure 4)**
```bash
python diagdevice.py
```
Real-time structural diagnostic tool for composite integers.  
> To test custom integers, edit `p1, q1` or `p2, q2` directly inside `diagdevice.py` (lines 81–115).

____________________________________________________________________________
**5. B-Smooth Spectral Analysis [NEW]**
```bash
python jinx_smooth.py
```
Validates spectral decay O(k^{-1/pi(B)}) for B-smooth number sets at resolution N=2^20.  
Empirical confirmation of Theorem 4.3 from the GNFS paper (Dickman polytope framework).

| B  | pi(B) | Smooth count | Observed slope |
|----|-------|-------------|----------------|
| 7  | 4     | 1,286       | -0.436         |
| 13 | 6     | 4,167       | -0.533         |
| 31 | 11    | 18,469      | -0.649         |
| 97 | 25    | 74,318      | -0.756         |
| Random | — | —         | -0.001 (baseline) |

____________________________________________________________________________
**6. Spectral Sieve Pre-filtering :: QS+Jinx [NEW]**
```bash
python jinx_qs.py
```
Proof-of-concept SSP: Jinx resonance score as pre-filter before smoothness testing.  
Gain G(τ) > 1 proven (Theorem 5.3) and confirmed empirically.

| N          | digits | Filter% | Gain G  |
|------------|--------|---------|---------|
| 1026601    | 7      | 49.3%   | ×1.87   |
| 190115299  | 9      | 67.0%   | ×2.88   |
| 9972830459 | 10     | 81.8%   | ×5.49   |

> Optimal threshold: τ = 0.3 — eliminates ~67% of candidates, retains ≥95% of smooth relations.

---

### Experimental Results Summary

**Table 1: Spectral scaling law validation.**

| Set                | Degree d | Predicted | Observed           |
|--------------------|----------|-----------|--------------------|
| Perfect squares n² | 2        | k^-1/2    | k^-0.48 ± 0.02     |
| Perfect cubes n³   | 3        | k^-1/3    | k^-0.34 ± 0.03     |
| Prime Numbers      | —        | Irregular | 0.91 ± 0.42        |

---

### Citation and Theory

This work is part of the **Cymalogy Corpus**, built on three layers:

1. **Nitescence Theorem** (logic) — DOI: [10.5281/zenodo.15466643](https://doi.org/10.5281/zenodo.15466643)
2. **Jinx's Theorem** (spectral arithmetic) — DOI: [10.5281/zenodo.18930421](https://doi.org/10.5281/zenodo.18930421)
3. **GNFS Spectral Bridge** (cryptographic applications) — in preparation (2026)

### BibTeX
```bibtex
@article{regent2026jinx,
  title     = {The Jinx's Theorem: Spectral Fingerprinting of Arithmetic Structures
               Through Quantum Resonance},
  author    = {R{\'e}gent, Xavier J.},
  year      = {2026},
  doi       = {10.5281/zenodo.18930421}
}

@unpublished{regent2026gnfs,
  title     = {From Undecidability to Cryptographic Efficiency: A Spectral Bridge
               from the Nitescence Theorem to Arithmetic Structure and Sieve Acceleration},
  author    = {R{\'e}gent, Xavier J.},
  year      = {2026},
  note      = {In preparation}
}
```
