

from abc import ABC, abstractmethod
from typing import List
from store.checkout.discount import Discount
from store.checkout.pricing_rule import PricingRule

from store.checkout.product import Product


class DiscountCalculator(ABC):

    pricing_rules: List[PricingRule]

    @abstractmethod
    def scan(self, product: Product) -> None:
        pass

    @abstractmethod
    def get_discounts(self) -> List[Discount]:
        pass


class DiscountCalculatorImpl(DiscountCalculator):

    def scan(self, product: Product) -> None:
        pass
    
    def get_discounts(self) -> List[Discount]:
        pass