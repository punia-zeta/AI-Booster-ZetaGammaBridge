"""
Core implementation of ZetaGammaBridge (double-precision).

This module implements a simple algebraic packaging of ζ(3) and γ:

    C₁ = ζ(3) * exp(1 - 1/γ)
    C₂ = ζ(3) * exp(1/γ - 1)

These constants satisfy the exact identity:

    C₁ * C₂ = ζ(3)²

The construction follows directly from the elementary identity eᵃ · e⁻ᵃ = 1.
It does not introduce a new mathematical relation between the two constants.
"""

from __future__ import annotations

import math
from typing import Optional


class ZetaGammaBridge:
    """
    Double-precision bridge between Apéry's constant ζ(3) and Euler-Mascheroni γ.

    Parameters
    ----------
    None
        Constants are initialised to standard double-precision values.
    """

    def __init__(self) -> None:
        # Standard double-precision reference values
        self.zeta3: float = 1.2020569031595942
        self.gamma: float = 0.5772156649015329

        self.C1: float = self.zeta3 * math.exp(1.0 - 1.0 / self.gamma)
        self.C2: float = self.zeta3 * math.exp(1.0 / self.gamma - 1.0)

    def zeta3_fast(self, n_terms: int = 27) -> float:
        """
        Evaluate ζ(3) using Apéry's accelerated series.

        The series is:

            ζ(3) = (5/2) Σ_{n=1}^∞ (-1)^{n-1} / (n³ * binom(2n, n))

        Parameters
        ----------
        n_terms : int, optional
            Number of terms to sum (default 27 ≈ 15 decimal places).

        Returns
        -------
        float
            Approximation of ζ(3).
        """
        if n_terms < 1:
            raise ValueError("n_terms must be at least 1")

        total = 0.0
        binom = 1.0  # becomes C(2n, n)

        for n in range(1, n_terms + 1):
            # C(2n, n) = C(2n-2, n-1) * (4n-2)/n
            # For n=1 this correctly yields C(2,1) = 2
            binom *= (4 * n - 2) / n
            term = ((-1) ** (n - 1)) / (n ** 3 * binom)
            total += term

        return 2.5 * total

    def gamma_from_C1(self, zeta3: Optional[float] = None) -> float:
        """
        Reconstruct γ from C₁ and ζ(3).

        Formula
        -------
        γ = 1 / (1 + ln(ζ(3)/C₁))
        """
        z = self.zeta3 if zeta3 is None else zeta3
        return 1.0 / (1.0 + math.log(z / self.C1))

    def gamma_from_C2(self, zeta3: Optional[float] = None) -> float:
        """
        Reconstruct γ from C₂ and ζ(3).

        Formula
        -------
        γ = 1 / (1 - ln(ζ(3)/C₂))
        """
        z = self.zeta3 if zeta3 is None else zeta3
        return 1.0 / (1.0 - math.log(z / self.C2))

    def verify_identity(self, tol: float = 1e-15) -> bool:
        """
        Verify the algebraic identity C₁ * C₂ == ζ(3)².

        Parameters
        ----------
        tol : float
            Absolute tolerance for the comparison.

        Returns
        -------
        bool
            True if the identity holds within the given tolerance.
        """
        return abs(self.C1 * self.C2 - self.zeta3 ** 2) < tol

    def memory_info(self) -> dict:
        """
        Return a transparent summary of the storage trade-off.

        Returns
        -------
        dict
            Dictionary containing byte counts and reduction percentage.
        """
        traditional = 16  # ζ(3) + γ
        with_c1_only = 8  # store only C₁
        return {
            "traditional_bytes": traditional,
            "c1_only_bytes": with_c1_only,
            "reduction_percent": 50.0,
            "note": (
                "Storing only C₁ saves 8 bytes at the cost of recomputing "
                "ζ(3) on demand (~0.04 ms). This is a space-time trade-off, "
                "not data compression."
            ),
        }
