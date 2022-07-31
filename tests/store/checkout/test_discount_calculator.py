from typing import List, Optional
import unittest
from unittest.mock import MagicMock
from store.checkout.discount import Discount

from store.checkout.discount_calculator import DiscountCalculator, DiscountCalculatorImpl
from store.checkout.pricing_rule import PricingRule, TShirtRule, VoucherRule
from store.checkout.product import Code, Product

class DiscountCalculatorTestCase(unittest.TestCase):

    def setup_pricing_rules_mocks(self) -> List[PricingRule]:
        """Setup for a list of pricing rules with scan method mocked"""
        pricing_rules: List[PricingRule] = []

        pricing_rule: PricingRule = VoucherRule("Voucher rule")
        pricing_rule.scan = MagicMock()
        pricing_rules.append(pricing_rule)

        pricing_rule = TShirtRule("TShirt rule")
        pricing_rule.scan = MagicMock()
        pricing_rules.append(pricing_rule)

        return pricing_rules

    def setup_products(self) -> List[Product]:
        """Setup for a list of products"""

        products: List[Product] = []
        products.append(Product(code=Code.VOUCHER, name="Gift Card", price=5.00))
        products.append(Product(code=Code.TSHIRT, name="Summer T-Shirt", price=20.0))
        products.append(Product(code=Code.PANTS, name="Summer Pants", price=7.5))
        return products

    def test_scan_call(self):
        """Test that for every product it calls the scan method once"""

        # Setup
        pricing_rules: List[PricingRule] = self.setup_pricing_rules_mocks()

        dc : DiscountCalculator = DiscountCalculatorImpl(pricing_rules=pricing_rules)
        dc.scan = MagicMock()
            
        products: List[Product] = self.setup_products()
        
        # Test

        for product in products:
            dc.scan(product)

        for index, pr in enumerate(pricing_rules):
            magic_mock : MagicMock = pr.scan  # type: ignore
            magic_mock.assert_called_once_with(products[index])
    
    def test_discounts_return(self):
        """Tests that dicount calculator returns list of discounts"""

        # Setup
        pricing_rules: List[PricingRule] = self.setup_pricing_rules_mocks()

        discounts: List[Discount] = []
        discounts.append(Discount(name="1", discount=1.0))
        discounts.append(Discount(name="2", discount=2.0))
        
        for index, pr in enumerate(pricing_rules):
            pr.get_discount = MagicMock(return_value=discounts[index])

        dc : DiscountCalculator = DiscountCalculatorImpl(pricing_rules=pricing_rules)

        # Test
        self.assertEqual(dc.get_discounts(), discounts)

        for pr in pricing_rules:
            magic_mock : MagicMock = pr.get_discount  # type: ignore
            magic_mock.assert_called_once()
    
    def test_no_discounts(self):
        """Tests that discount calculator returns an empty list for no discounts"""

        # Setup
        pricing_rules: List[PricingRule] = self.setup_pricing_rules_mocks()

        for pr in pricing_rules:
            pr.get_discount = MagicMock(return_value=None)

        dc : DiscountCalculator = DiscountCalculatorImpl(pricing_rules=pricing_rules)

        # Test
        self.assertEqual(dc.get_discounts(), [])

        for pr in pricing_rules:
            magic_mock : MagicMock = pr.get_discount  # type: ignore
            magic_mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()