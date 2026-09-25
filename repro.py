"""Reproduction script for inverted discount operator in pricing."""
import sys
from decimal import Decimal
from pricing import apply_discount

if __name__ == "__main__":
    subtotal = Decimal("100.00")
    discount = Decimal("20")  # 20% off
    expected = Decimal("80.00")

    actual = apply_discount(subtotal, discount)
    if actual == expected:
        print(f"PASS: apply_discount returned {actual}")
        sys.exit(0)
    else:
        sys.stderr.write(
            f"REPRODUCED Defect: Expected discounted total {expected}, but got {actual} (subtotal increased instead of decreased)\n"
        )
        sys.exit(1)
