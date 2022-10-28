from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional
import unittest
from src.store.checkout.discount import Discount
from src.store.checkout.pricing_rule import PricingRule

from src.store.checkout.product import Product

@dataclass
class DiscountCalculator(ABC):
    """Calculates the discount of products"""

    pricing_rules: List[PricingRule]

    @abstractmethod
    def scan(self, product: Product) -> None:
        """Scans the product for each pricing rule"""
        pass

    @abstractmethod
    def get_discounts(self) -> List[Discount]:
        """Retrieves the list of discounts of the pricing rules"""
        pass

@dataclass
class DiscountCalculatorImpl(DiscountCalculator):
    """Calculates the discount of products"""

    def scan(self, product: Product) -> None:
        """Scans the product for each pricing rule"""

        for pr in self.pricing_rules:
            pr.scan(product=product)
    
    def get_discounts(self) -> List[Discount]:
        """Retrieves the list of discounts of the pricing rules"""
        
        discounts: List[Discount] = []

        for pr in self.pricing_rules:
            
            discount: Optional[Discount] = pr.get_discount()

            if discount is not None:
                discounts.append(discount)

        return discounts

if __name__ == '__main__':
    unittest.main()