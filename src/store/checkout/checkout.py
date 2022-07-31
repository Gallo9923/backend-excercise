from dataclasses import dataclass, field
from typing import List

from store.checkout.pricing_rule import PricingRule
from store.checkout.discount_calculator import DiscountCalculator
from store.checkout.calculator import Calculator
from store.checkout.product import Product

@dataclass
class Checkout():
    """Calculates the total price of a checkout of products with discounts"""

    products: List[Product] = field(init=False)
    discount_calculator: DiscountCalculator
    calculator: Calculator

    def scan(self, product: Product) -> None:
        pass

    def get_total(self) -> float:
        pass
