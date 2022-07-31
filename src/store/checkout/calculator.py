from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List

from store.checkout.product import Product
from store.checkout.discount import Discount


@dataclass
class Calculator(ABC):
    """Calculates the price of a checkout"""

    @abstractmethod
    def get_total(self, products: List[Product], discounts: List[Discount]) -> float:
        pass


@dataclass
class CalculatorImpl(Calculator):
    """Calculates the price of a checkout"""

    def get_total(self, products: List[Product], discounts: List[Discount]) -> float:
        pass