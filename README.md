# AI Booster v1.0.1 — Core ZetaGammaBridge

**Algebraic packaging of Apéry’s constant ζ(3) and the Euler-Mascheroni constant γ**

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21839959-blue)](https://doi.org/10.5281/zenodo.21839959)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## Overview

This repository provides a clean, lightweight Python implementation of an algebraic packaging between:

- **Apéry’s constant**: ζ(3) ≈ 1.2020569031595942  
- **Euler-Mascheroni constant**: γ ≈ 0.5772156649015329

The bridge constants are defined as:

\[
C_1 = \zeta(3)\, e^{1 - 1/\gamma}, \qquad
C_2 = \zeta(3)\, e^{1/\gamma - 1}
\]

They satisfy the exact elementary identity

\[
C_1 \times C_2 = \zeta(3)^2
\]

and γ can be recovered in constant time by

\[
\gamma = \frac{1}{1 + \ln(\zeta(3)/C_1)}.
\]

This is an algebraic re-packaging that follows directly from the identity \(e^a \cdot e^{-a} = 1\). It is **not** a new mathematical theorem relating ζ(3) and γ, but it provides a convenient form for numerical checks and a simple storage trade-off.

---

## Features

- **27-step Apéry accelerator** – recovers ζ(3) to ~15 decimal places in ≈ 0.04 ms
- **17-step fast mode** – approximately 1.6× faster
- **Memory trade-off** – store only \(C_1\) (8 bytes) instead of ζ(3) + γ (16 bytes) → **50% reduction**, at the cost of recomputing ζ(3) on demand
- **O(1) numerical integrity check** – verifies \(C_1 \times C_2 = \zeta(3)^2\) (useful as a fast checksum, not a cryptographic hash)
- **High-precision support** – optional `Decimal`-based implementation (default 50 digits)
- **Pure Python** – zero runtime dependencies (Python 3.8+)

---

## Installation

```bash
git clone https://github.com/punia-zeta/AI-Booster-ZetaGammaBridge.git
cd AI-Booster-ZetaGammaBridge
pip install -e .
