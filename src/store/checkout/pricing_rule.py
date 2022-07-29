from dataclasses import dataclass
from abc import ABC, abstractmethod

from store.checkout.product import Product
from store.checkout.discount import Discount

@dataclass
class PricingRule(ABC):
    """Represents the abstract class of a pricing rule for applying a discount strategy"""

    name: str

    @abstractmethod
    def scan(product: Product):
        pass

    @abstractmethod
    def get_discount() -> Discount: 
        pass


@dataclass
class VoucherRule(PricingRule):
    """Discount applied to Voucher type products"""

    def scan(product: Product):
        pass

    def get_discount() -> Discount: 
        pass


@dataclass
class TShirtRule(PricingRule):
    """Discount applied to TShirt type products"""

    def scan(product: Product):
        pass

    def get_discount() -> Discount: 
        pass