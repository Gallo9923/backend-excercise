import unittest
from unittest.mock import Mock, MagicMock
from typing import List
from store.checkout.calculator import Calculator, CalculatorImpl

from store.checkout.checkout import Checkout
from store.checkout.discount import Discount
from store.checkout.discount_calculator import DiscountCalculator, DiscountCalculatorImpl
from store.checkout.pricing_rule import PricingRule
from store.checkout.product import Code, Product


class CheckoutTestCase(unittest.TestCase):


    def test_scan_products(self):
        """Tests that every product was scanned"""
        
        # Setup
        pricing_rules: List[PricingRule] = Mock()
        
        discount_calculator: DiscountCalculator = DiscountCalculatorImpl(pricing_rules)
        discount_calculator.scan = MagicMock()

        calculator: Calculator = Mock()

        c: Checkout = Checkout(discount_calculator=discount_calculator , calculator=calculator)

        products: List[Product] = []
        products.append(Product(code=Code.VOUCHER, name="Gift Card", price=5.00))
        products.append(Product(code=Code.TSHIRT, name="Summer T-Shirt", price=20.0))
        products.append(Product(code=Code.PANTS, name="Summer Pants", price=7.5))

        # Test  
        for product in products:
            c.scan(product=product)
            discount_calculator.scan.assert_called_with(product=product)

        self.assertEqual(c.products, products)

    def test_get_discounts(self):
        """Tests that get_discounts was called"""
        
        # Setup
        discounts: List[Discount] = []
        discounts.append(Discount(name="1", discount=1.0))

        pricing_rules: List[PricingRule] = Mock()
        
        discount_calculator: DiscountCalculator = DiscountCalculatorImpl(pricing_rules)
        discount_calculator.scan = MagicMock()
        discount_calculator.get_discounts = MagicMock(return_value=discounts)

        calculator: Calculator = CalculatorImpl()
        calculator.get_total = MagicMock()

        c: Checkout = Checkout(discount_calculator=discount_calculator , calculator=calculator)

        products: List[Product] = []
        products.append(Product(code=Code.VOUCHER, name="Gift Card", price=5.00))
        products.append(Product(code=Code.TSHIRT, name="Summer T-Shirt", price=20.0))
        products.append(Product(code=Code.PANTS, name="Summer Pants", price=7.5))

        # Test    
        c.get_total()
        discount_calculator.get_discounts.assert_called_once()


    def test_get_total(self):
        """Tests that get_total was called with the correct values"""

        # Setup
        discounts: List[Discount] = []
        discounts.append(Discount(name="1", discount=7.50))

        pricing_rules: List[PricingRule] = Mock()
        
        discount_calculator: DiscountCalculator = DiscountCalculatorImpl(pricing_rules)
        discount_calculator.scan = MagicMock()
        discount_calculator.get_discounts = MagicMock(return_value=discounts)

        calculator: Calculator = CalculatorImpl()
        calculator.get_total = MagicMock(return_value=25.0)
        
        products: List[Product] = []
        products.append(Product(code=Code.VOUCHER, name="Gift Card", price=5.00))
        products.append(Product(code=Code.TSHIRT, name="Summer T-Shirt", price=20.0))
        products.append(Product(code=Code.PANTS, name="Summer Pants", price=7.5))

        c: Checkout = Checkout(discount_calculator=discount_calculator , calculator=calculator)
        c.products = products

        # Test
        result: float = c.get_total()
        calculator.get_total.assert_called_once_with(products=products, discounts=discounts)
        self.assertAlmostEqual(result, 25)

if __name__ == '__main__':
    unittest.main()