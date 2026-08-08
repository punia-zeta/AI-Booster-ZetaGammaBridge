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
```

Or simply place the `zeta_bridge` package in your project.

---

## Quick Start

### Double precision

```python
from zeta_bridge import ZetaGammaBridge

bridge = ZetaGammaBridge()

print(bridge.zeta3)               # 1.2020569031595942
print(bridge.gamma)               # 0.5772156649015329
print(bridge.C1, bridge.C2)

# Apéry series
z = bridge.zeta3_fast(n_terms=27)
print(z)

# Reconstruct γ
g = bridge.gamma_from_C1()
print(g)

# Verify identity
print(bridge.verify_identity())   # True
```

### High precision

```python
from zeta_bridge import HighPrecisionBridge

hp = HighPrecisionBridge(precision=50)
hp.summary()

z = hp.zeta3_series(n_terms=45)
g = hp.gamma_from_C1()
print(hp.verify_identity())
```

---

## Mathematical Background

The implementation uses Apéry’s classical accelerated series:

\[
\zeta(3) = \frac{5}{2} \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^3 \binom{2n}{n}}
\]

Central binomial coefficients are computed via the recurrence

\[
\binom{2n}{n} = \binom{2n-2}{n-1} \cdot \frac{4n-2}{n}
\]

which is efficient and avoids intermediate overflow.

The bridge constants themselves add no new analytic information; they merely rewrite the pair \(( \zeta(3),\gamma )\) so that the product identity becomes trivial and γ can be recovered in \(O(1)\) time once ζ(3) is known.

---

## Storage Remark

| Approach              | Bytes | Notes                                      |
|-----------------------|-------|--------------------------------------------|
| Store ζ(3) + γ        | 16    | Direct                                     |
| Store only \(C_1\)    | 8     | Recompute ζ(3) on demand (≈ 0.04 ms)      |
| Reduction             | 50%   | Classic space–time trade-off, not compression |

---

## Running Tests

```bash
pip install -e ".[test]"
pytest tests/ -v
```

All 10 unit tests currently pass.

---

## Project Layout

```
zeta_bridge/
├── __init__.py
├── core.py              # Double-precision implementation
└── high_precision.py    # Decimal-based high-precision version
tests/
└── test_zeta_bridge.py
pyproject.toml
README.md
```

---

## Citation

```bibtex
@software{Punia2026ZetaGammaBridge,
  author    = {Punia, Manoj},
  title     = {AI Booster v1.0.1 — Core ZetaGammaBridge},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.21839959},
  url       = {https://doi.org/10.5281/zenodo.21839959}
}
```

---

## License

Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0).  
You may share the material for non-commercial purposes with proper attribution. Commercial use and derivative works require permission from the author.

---

## Author

**Manoj Punia**  
ORCID: [0009-0002-8186-7281](https://orcid.org/0009-0002-8186-7281)  
Email: mspunia1976@gmail.com

