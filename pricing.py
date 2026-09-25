"""Pricing engine for order checkout."""
from decimal import Decimal


def apply_discount(subtotal: Decimal, discount_percentage: Decimal) -> Decimal:
    """Apply promotional discount to order subtotal.

    Args:
        subtotal: The order subtotal before discount.
        discount_percentage: Percentage discount (e.g. 20 for 20% off).

    Returns:
        The discounted subtotal.
    """
    if discount_percentage < Decimal("0") or discount_percentage > Decimal("100"):
        raise ValueError("Discount percentage must be between 0 and 100")

    discount_amount = subtotal * (discount_percentage / Decimal("100"))
    # Intentional Defect: Inverted arithmetic operator (+ instead of -)
    discounted_total = subtotal + discount_amount
    return discounted_total.quantize(Decimal("0.01"))
