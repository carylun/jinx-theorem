# Jinx Theorem: Spectral Fingerprinting of Arithmetic Structures

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18263783.svg)](https://doi.org/10.5281/zenodo.18263783)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Paper](https://img.shields.io/badge/Paper-QIP%202026-blue)](https://link-to-paper-when-published)

Official repository for the paper: 

"The Jinx's Theorem: Spectral Fingerprinting of Arithmetic Structures Through Quantum Resonance" 

by Xavier J. Régent

----------------------------------------------------------------------

### Overview ### 

This repository provides the implementation of the Jinx's Theorem, demonstrating that arithmetic structures possess intrinsic, measurable spectral signatures. By shifting from enumerative complexity to spectral resonance, we provide a new framework for analyzing prime numbers, perfect powers, and composite integers. 

Key Features:
- Square Scan: Spectral signature of perfect squares (20-Qubit resolution).
- Millionaire Scan: Analysis of 82,000+ primes at 2^20 resolution.
- Riemann Alignment: Verification against the first 30 non-trivial zeros.
- Structural Triangulation: Real-time diagnostic of 70+ digit integers.


### Quick Start ### 

To reproduce the results presented in the paper, ensure you have these dependencies installed:

pip install numpy matplotlib qiskit qiskit-aer

----------------------------------------------------------------------

1. Universal Scaling Law :: Square Field (Figure 1)
   python jinx_square.py

   * Evidence of the fundamental k^-1/2 harmonic signature (20-Qubit).

----------------------------------------------------------------------

2. Riemann Resonance Alignment (Figure 2)
   python riemann.py

   * Visual correlation between Jinx peaks and the first 30 Zeta zeros.

----------------------------------------------------------------------

3. The Millionaire Scan :: Prime Field (Figure 3)
   python millionaire_scan.py

   * High-resolution analysis of 82,000+ primes at 2^20 states.

----------------------------------------------------------------------

4. Composite Triangulation :: Diagnostic Device (Figure 4)
   python diagdevice.py

   * Real-time structural diagnostic tool for composite integers.

   NOTE: To test custom integers, edit the p1, q1 or p2, q2
   variables directly inside diagdevice.py (lines 81-115).


### Experimental Results Summary ### 

Table 1: Spectral scaling law validation. 

Set                | Degree d | Predicted | Observed
-------------------|----------|-----------|------------------
Perfect squares n^2| 2        | k^-1/2    | k^-0.48 +/- 0.02
Perfect cubes n^3  | 3        | k^-1/3    | k^-0.34 +/- 0.03
Prime Numbers      | --       | Irregular | 0.91 +/- 0.42


### Citation and Theory ### 

This work is the applied counterpart of the Nitescence Theorem, which addresses the resolution of undecidability through structural relevance. 

DOI (Preprint/Theorem): 10.5281/zenodo.15466643

### BibTeX
```
@article{regent2026jinx,
  title={The Jinx's Theorem: Spectral Fingerprinting of Arithmetic Structures},
  author={R{\'e}gent, Xavier J.},
  journal={Quantum Information Processing},
  year={2026},
  note={Submitted}
}
```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
