from typing import List
import unittest

from store.checkout.calculator import Calculator, CalculatorImpl
from store.checkout.discount import Discount
from store.checkout.product import Code, Product

class CalculatorTestCase(unittest.TestCase):

    def test_no_discounts(self):
        """Tests that the calculator calculates correctly with no discounts"""

        products: List[Product] = []
        products.append(Product(code=Code.VOUCHER, name="Gift Card", price=5.00))
        products.append(Product(code=Code.TSHIRT, name="Summer T-Shirt", price=20.0))
        products.append(Product(code=Code.PANTS, name="Summer Pants", price=7.5))

        c: Calculator = CalculatorImpl()
        result: float = c.get_total(products=products, discounts=[])

        self.assertAlmostEqual(result, 32.5)


    def test_with_discount(self):
        """Tests that the calculator calculates correctly with no discounts"""
        
        discounts: List[Discount] = []
        discounts.append(Discount(name="Voucher discount", discount=5.0))

        products: List[Product] = []
        products.append(Product(code=Code.VOUCHER, name="Gift Card", price=5.00))
        products.append(Product(code=Code.TSHIRT, name="Summer T-Shirt", price=20.0))
        products.append(Product(code=Code.VOUCHER, name="Gift Card", price=5.00))

        c: Calculator = CalculatorImpl()
        result: float = c.get_total(products=products, discounts=discounts)

        self.assertAlmostEqual(result, 25.0)


    def test_with_negative_discounts(self):

        discounts: List[Discount] = []
        discounts.append(Discount(name="Voucher discount", discount=-5.0))

        products: List[Product] = []
        products.append(Product(code=Code.VOUCHER, name="Gift Card", price=5.00))
        products.append(Product(code=Code.TSHIRT, name="Summer T-Shirt", price=20.0))
        products.append(Product(code=Code.VOUCHER, name="Gift Card", price=5.00))

        c: Calculator = CalculatorImpl()
        result: float = c.get_total(products=products, discounts=discounts)
        
        self.assertAlmostEqual(result, 25.0)
