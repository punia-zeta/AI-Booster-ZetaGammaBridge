"""
ZetaGammaBridge
---------------
A clean algebraic packaging of Apéry's constant ζ(3) and the Euler-Mascheroni constant γ.

This package provides:
- Fast Apéry-series evaluation of ζ(3)
- Exact algebraic identities linking ζ(3) and γ via bridge constants C₁, C₂
- High-precision Decimal arithmetic support
- Simple reconstruction of γ from the bridge constants
"""

from .core import ZetaGammaBridge
from .high_precision import HighPrecisionBridge

__version__ = "1.0.1"
__author__ = "Manoj Punia"
__all__ = ["ZetaGammaBridge", "HighPrecisionBridge"]
