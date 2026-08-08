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

```
C₁ = ζ(3) · exp(1 - 1/γ)
C₂ = ζ(3) · exp(1/γ - 1)
```

They satisfy the exact elementary identity:

```
C₁ × C₂ = ζ(3)²
```

and γ can be recovered in constant time by:

```
γ = 1 / (1 + ln(ζ(3)/C₁))
```

This is an algebraic re-packaging that follows directly from the identity `eᵃ · e⁻ᵃ = 1`.  
It is **not** a new mathematical theorem relating ζ(3) and γ.

---

## Features

- **27-step Apéry accelerator** – recovers ζ(3) to ~15 decimal places in ≈ 0.04 ms
- **17-step fast mode** – approximately 1.6× faster
- **Memory trade-off** – store only C₁ (8 bytes) instead of ζ(3) + γ (16 bytes) → **50% reduction**
- **O(1) numerical integrity check** – verifies `C₁ × C₂ = ζ(3)²`
- **High-precision support** – optional `Decimal`-based implementation (default 50 digits)
- **Pure Python** – zero runtime dependencies (Python 3.8+)

---

## Installation

```bash
git clone https://github.com/punia-zeta/AI-Booster-ZetaGammaBridge.git
cd AI-Booster-ZetaGammaBridge
pip install -e .
```

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

## Project Structure

```
AI-Booster-ZetaGammaBridge/
├── zeta_bridge/
│   ├── __init__.py
│   ├── core.py              # Double-precision implementation
│   └── high_precision.py    # Decimal high-precision version
├── pyproject.toml
└── README.md
```

---

## Mathematical Background

The implementation uses Apéry’s classical accelerated series:

```
ζ(3) = (5/2) Σ (-1)^{n-1} / (n³ · binom(2n, n))
```

Central binomial coefficients are computed via the recurrence:

```
binom(2n, n) = binom(2n-2, n-1) · (4n-2)/n
```

---

## Storage Remark

| Approach           | Bytes | Notes                                      |
|--------------------|-------|--------------------------------------------|
| Store ζ(3) + γ     | 16    | Direct                                     |
| Store only C₁      | 8     | Recompute ζ(3) on demand (≈ 0.04 ms)      |
| Reduction          | 50%   | Classic space–time trade-off               |

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
You may share the material for non-commercial purposes with proper attribution.  
Commercial use and derivative works require permission from the author.

---

## Author

**Manoj Punia**  
ORCID: [0009-0002-8186-7281](https://orcid.org/0009-0002-8186-7281)  
Email: mspunia1976@gmail.com

---

*Version 1.0.1 — August 2026*
```


डालने के बाद बता दें, मैं एक बार फिर चेक कर लूँगा।
