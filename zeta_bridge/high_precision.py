"""
High-precision implementation using decimal.Decimal.

This module provides a Decimal-based version of the bridge for
arbitrary precision arithmetic (default 50 decimal places).
"""

from __future__ import annotations

from decimal import Decimal, getcontext
from typing import Optional

# Set working precision
getcontext().prec = 50

# High-precision reference values (more digits than double)
ZETA3_HP = Decimal(
    "1.2020569031595942853997381615114499907649862923404988817922715553418382"
)
GAMMA_HP = Decimal(
    "0.5772156649015328606065120900824024310421593359399235988057672348848677"
)


class HighPrecisionBridge:
    """
    Arbitrary-precision bridge between ζ(3) and γ using decimal.Decimal.

    Parameters
    ----------
    precision : int, optional
        Number of significant digits (default 50).
    """

    def __init__(self, precision: int = 50) -> None:
        if precision < 20:
            raise ValueError("precision should be at least 20")
        getcontext().prec = precision

        self.precision = precision
        self.zeta3 = ZETA3_HP
        self.gamma = GAMMA_HP

        one = Decimal(1)
        self.C1 = self.zeta3 * (one - one / self.gamma).exp()
        self.C2 = self.zeta3 * (one / self.gamma - one).exp()

    def zeta3_series(self, n_terms: int = 40) -> Decimal:
        """
        Evaluate ζ(3) with the Apéry series using Decimal arithmetic.

        More terms are required than in double precision to reach
        the working precision.

        Parameters
        ----------
        n_terms : int
            Number of terms (40 is usually sufficient for 50 digits).

        Returns
        -------
        Decimal
            High-precision approximation of ζ(3).
        """
        if n_terms < 1:
            raise ValueError("n_terms must be at least 1")

        total = Decimal(0)
        binom = Decimal(1)

        for n in range(1, n_terms + 1):
            # C(2n, n) = C(2n-2, n-1) * (4n-2)/n
            binom *= Decimal(4 * n - 2) / Decimal(n)
            sign = Decimal(1) if (n % 2 == 1) else Decimal(-1)
            term = sign / (Decimal(n) ** 3 * binom)
            total += term

        return Decimal("2.5") * total

    def gamma_from_C1(self, zeta3: Optional[Decimal] = None) -> Decimal:
        """Reconstruct γ from C₁ and ζ(3) at high precision."""
        z = self.zeta3 if zeta3 is None else zeta3
        return Decimal(1) / (Decimal(1) + (z / self.C1).ln())

    def gamma_from_C2(self, zeta3: Optional[Decimal] = None) -> Decimal:
        """Reconstruct γ from C₂ and ζ(3) at high precision."""
        z = self.zeta3 if zeta3 is None else zeta3
        return Decimal(1) / (Decimal(1) - (z / self.C2).ln())

    def verify_identity(self, tol: Optional[Decimal] = None) -> bool:
        """
        Verify C₁ * C₂ == ζ(3)² at the current precision.

        Parameters
        ----------
        tol : Decimal, optional
            Absolute tolerance. Defaults to 10^(1-precision).
        """
        if tol is None:
            tol = Decimal(10) ** (1 - self.precision)
        left = self.C1 * self.C2
        right = self.zeta3 ** 2
        return abs(left - right) < tol

    def summary(self) -> None:
        """Print a short high-precision summary."""
        print(f"Precision     : {self.precision} digits")
        print(f"ζ(3)          : {self.zeta3}")
        print(f"γ             : {self.gamma}")
        print(f"C₁            : {self.C1}")
        print(f"C₂            : {self.C2}")
        print(f"Identity holds: {self.verify_identity()}")
