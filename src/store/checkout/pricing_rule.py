from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Optional

from store.checkout.product import Product, Code
from store.checkout.discount import Discount

@dataclass
class PricingRule(ABC):
    """Represents the abstract class of a pricing rule for applying a discount strategy"""

    name: str

    @abstractmethod
    def scan(self, product: Product):
        pass

    @abstractmethod
    def get_discount(self) -> Optional[Discount]: 
        pass


@dataclass
class VoucherRule(PricingRule):
    """Discount applied to Voucher type products"""

    voucher_counter: int = field(init=False, default=0)

    def scan(self, product: Product) -> None:
        """Scans a product"""

        if product.code == Code.VOUCHER: self.voucher_counter += 1

    def get_discount(self) -> Optional[Discount]: 
        """Calculates the discount of voucher items"""

        discount_counter = self.voucher_counter // 2
        
        if discount_counter == 0:
            return None
        elif discount_counter > 0:
            discount_applied = discount_counter * 5.0
            return Discount(self.name, discount_applied)


@dataclass
class TShirtRule(PricingRule):
    """Discount applied to TShirt type products"""

    def scan(self, product: Product):
        pass

    def get_discount(self) -> Optional[Discount]: 
        pass