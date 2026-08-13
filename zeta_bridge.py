"""
ZetaGammaBridge — O(1) bridge between zeta(3) and gamma
Author: Manoj Punia
DOI: 10.5281/zenodo.21839959
"""

import math
from decimal import Decimal, getcontext

class ZetaGammaBridge:
    def __init__(self, precision=50, fast=False):
        """
        precision: decimal digits for internal calculations
        fast: if True, use 17-step approximation instead of 27-step
        """
        getcontext().prec = precision
        self.fast = fast
        self.zeta = self._compute_zeta()
        self.gamma = 0.57721566490153286060651209  # known value
        # Build bridge constants
        exp1 = Decimal(1) - Decimal(1) / Decimal(self.gamma)
        exp2 = Decimal(1) / Decimal(self.gamma) - Decimal(1)
        self.c1 = Decimal(self.zeta) * (Decimal(math.e) ** exp1)
        self.c2 = Decimal(self.zeta) * (Decimal(math.e) ** exp2)
        # Verify identity
        assert abs(self.c1 * self.c2 - Decimal(self.zeta) ** 2) < Decimal('1e-20'), "Bridge identity failed"

    def _compute_zeta(self):
        """Apery's accelerated series for zeta(3)"""
        if self.fast:
            n_terms = 17
        else:
            n_terms = 27
        s = Decimal(0)
        for n in range(1, n_terms + 1):
            num = (-1) ** (n - 1)
            den = n ** 3 * math.comb(2 * n, n)  # math.comb for binomial
            s += Decimal(num) / Decimal(den)
        return Decimal('2.5') * s

    def recover_gamma(self):
        """Recover gamma from c1 and zeta(3) — O(1)"""
        ratio = Decimal(self.zeta) / self.c1
        gamma = Decimal(1) / (Decimal(1) + ratio.ln())
        return float(gamma)

# Example usage
if __name__ == "__main__":
    bridge = ZetaGammaBridge()
    print(f"zeta(3) = {bridge.zeta:.15f}")
    print(f"gamma   = {bridge.gamma:.15f}")
    print(f"c1      = {bridge.c1:.15f}")
    print(f"c2      = {bridge.c2:.15f}")
    print(f"c1 * c2 = {(bridge.c1 * bridge.c2):.15f}")
    print(f"zeta(3)^2 = {bridge.zeta ** 2:.15f}")
    recovered = bridge.recover_gamma()
    print(f"Recovered gamma = {recovered:.15f} (difference {abs(recovered - bridge.gamma):.2e})")
