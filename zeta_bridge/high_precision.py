"""
High-precision implementation using decimal.Decimal.

This module provides a Decimal-based version of the bridge for
arbitrary precision arithmetic (default 50 decimal places).
"""

from __future__ import annotations

from decimal import Decimal, getcontext
from typing import Optional

# Default working precision configuration
getcontext().prec = 50

# High-precision reference values (70+ digits to support deep initialization)
ZETA3_HP = Decimal(
    "1.2020569031595942853997381615114499907649862923404988817922715553418382"
)
GAMMA_HP = Decimal(
    "0.5772156649015328606065120900824024310421593359399235988057672348848677"
)


class HighPrecisionBridge:
    """Arbitrary-precision bridge between ζ(3) and γ using decimal.Decimal."""

    def __init__(self, precision: int = 50) -> None:
        """Initializes constants and calculates high-precision bridge values.

        Args:
            precision: Number of significant digits (default 50).

        Raises:
            ValueError: If precision is less than 20.
        """
        if precision < 20:
            raise ValueError("precision should be at least 20")

        # Set the desired working precision for global Decimal execution context
        getcontext().prec = precision

        self.precision = precision
        self.zeta3 = ZETA3_HP
        self.gamma = GAMMA_HP

        one = Decimal(1)
        # C1 = ζ(3) * exp(1 - 1/γ)
        self.C1 = self.zeta3 * (one - one / self.gamma).exp()
        # C2 = ζ(3) * exp(1/γ - 1)
        self.C2 = self.zeta3 * (one / self.gamma - one).exp()

    def zeta3_series(self, n_terms: int = 45) -> Decimal:
        """Evaluates ζ(3) with the Apéry series using Decimal arithmetic.

        More terms are required than in double precision to reach
        deep working precision bounds.

        Args:
            n_terms: Number of series loop steps (default 45).

        Returns:
            Decimal: High-precision approximation of ζ(3).

        Raises:
            ValueError: If n_terms is less than 1.
        """
        if n_terms < 1:
            raise ValueError("n_terms must be at least 1")

        total = Decimal(0)
        binom = Decimal(1)

        for n in range(1, n_terms + 1):
            # Update central binomial coefficient recurrence: C(2n, n)
            binom *= Decimal(4 * n - 2) / Decimal(n)
            sign = Decimal(1) if (n % 2 == 1) else Decimal(-1)
            term = sign / (Decimal(n) ** 3 * binom)
            total += term

        return Decimal("2.5") * total

    def gamma_from_C1(self, zeta3: Optional[Decimal] = None) -> Decimal:
        """Reconstructs γ from C₁ and ζ(3) at high precision.

        Args:
            zeta3: Optional override for the high-precision value of ζ(3).

        Returns:
            Decimal: The recovered value of γ.
        """
        z = self.zeta3 if zeta3 is None else zeta3
        one = Decimal(1)
        return one / (one + (z / self.C1).ln())

    def gamma_from_C2(self, zeta3: Optional[Decimal] = None) -> Decimal:
        """Reconstructs γ from C₂ and ζ(3) at high precision.

        Args:
            zeta3: Optional override for the high-precision value of ζ(3).

        Returns:
            Decimal: The recovered value of γ.
        """
        z = self.zeta3 if zeta3 is None else zeta3
        one = Decimal(1)
        return one / (one - (z / self.C2).ln())

    def verify_identity(self, tol: Optional[Decimal] = None) -> bool:
        """Verifies that C₁ * C₂ == ζ(3)² within target precision limits.

        Args:
            tol: Absolute tolerance limit threshold. Defaults to 10^(1-precision).

        Returns:
            bool: True if the structural identity maps within tolerance bounds.
        """
        if tol is None:
            tol = Decimal(10) ** (1 - self.precision)
        left = self.C1 * self.C2
        right = self.zeta3 ** 2
        return abs(left - right) < tol

    def summary(self) -> None:
        """Outputs calculation performance statistics metrics."""
        print(f"Precision      : {self.precision} digits")
        print(f"ζ(3)          : {self.zeta3}")
        print(f"γ             : {self.gamma}")
        print(f"C₁            : {self.C1}")
        print(f"C₂            : {self.C2}")
        print(f"Identity holds: {self.verify_identity()}")
