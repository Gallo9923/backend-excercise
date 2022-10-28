from dataclasses import dataclass, field
from typing import List

from src.store.checkout.discount_calculator import DiscountCalculator
from src.store.checkout.calculator import Calculator
from src.store.checkout.product import Product
from src.store.checkout.discount import Discount

@dataclass
class Checkout():
    """Calculates the total price of a checkout of products with discounts"""

    products: List[Product] = field(init=False)
    discount_calculator: DiscountCalculator
    calculator: Calculator

    def __post_init__(self):
        self.products = []


    def scan(self, product: Product) -> None:
        """Scans the product"""

        self.discount_calculator.scan(product=product)
        self.products.append(product)


    def get_total(self) -> float:
        """Calculates the total to pay of the checkout"""
        
        discounts: List[Discount] = self.discount_calculator.get_discounts()
        total: float = self.calculator.get_total(products=self.products, discounts=discounts)
        return total