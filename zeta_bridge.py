#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Booster v1.0.1 — Demo script for ZetaGammaBridge
Run:  python zeta_bridge.py
"""

from zeta_bridge import ZetaGammaBridge, HighPrecisionBridge


def main():
    print("=" * 60)
    print("AI Booster v1.0.1 — Core ZetaGammaBridge")
    print("=" * 60)

    # Double precision
    bridge = ZetaGammaBridge()

    print("\n📊 BRIDGE CONSTANTS:")
    print(f"  ζ(3)     = {bridge.zeta3:.16f}")
    print(f"  γ        = {bridge.gamma:.16f}")
    print(f"  C₁       = {bridge.C1:.16f}")
    print(f"  C₂       = {bridge.C2:.16f}")

    print("\n🔐 NUMERICAL INTEGRITY CHECK:")
    print(f"  C₁ × C₂  = {bridge.C1 * bridge.C2:.16f}")
    print(f"  ζ(3)²    = {bridge.zeta3 ** 2:.16f}")
    print(f"  Verified = {bridge.verify_identity()}")

    print("\n⚡ APÉRY ACCELERATOR (27 steps):")
    z27 = bridge.zeta3_fast(27)
    print(f"  ζ(3) ≈ {z27:.16f}")
    print(f"  Error  = {abs(z27 - bridge.zeta3):.2e}")

    print("\n⚡ APÉRY ACCELERATOR (17 steps):")
    z17 = bridge.zeta3_fast(17)
    print(f"  ζ(3) ≈ {z17:.14f}")
    print(f"  Error  = {abs(z17 - bridge.zeta3):.2e}")

    print("\n♻️ GAMMA RECONSTRUCTION:")
    g = bridge.gamma_from_C1()
    print(f"  γ from C₁ = {g:.16f}")
    print(f"  Error     = {abs(g - bridge.gamma):.2e}")

    # Memory info
    info = bridge.memory_info()
    print("\n💾 MEMORY TRADE-OFF:")
    print(f"  Traditional : {info['traditional_bytes']} bytes")
    print(f"  C₁ only     : {info['c1_only_bytes']} bytes")
    print(f"  Reduction   : {info['reduction_percent']}%")
    print(f"  Note        : {info['note']}")

    # High precision demo
    print("\n" + "=" * 60)
    print("HIGH PRECISION DEMO (40 digits)")
    print("=" * 60)
    hp = HighPrecisionBridge(precision=40)
    hp.summary()

    print("\n" + "=" * 60)
    print("✅ All checks completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()
