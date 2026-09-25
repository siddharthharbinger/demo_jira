from decimal import Decimal
from pricing import apply_discount


def test_apply_discount_standard():
    assert apply_discount(Decimal("100.00"), Decimal("20")) == Decimal("80.00")


def test_apply_discount_zero():
    assert apply_discount(Decimal("50.00"), Decimal("0")) == Decimal("50.00")
