from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List

from store.checkout.product import Product
from store.checkout.discount import Discount


@dataclass
class Calculator(ABC):
    
    @abstractmethod
    def get_total(self, products: List[Product], discounts: List[Discount]) -> str:
        pass


@dataclass
class CalculatorImpl(Calculator):

    @abstractmethod
    def get_total(self, products: List[Product], discounts: List[Discount]) -> str:
        pass