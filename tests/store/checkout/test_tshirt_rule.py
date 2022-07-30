from typing import List, Optional
import unittest
from store.checkout.discount import Discount

from store.checkout.pricing_rule import TShirtRule
from store.checkout.product import Code, Product

class TShirtRuleTestCase(unittest.TestCase):

    tsr: Optional[TShirtRule] = None
    
    def setUp(self) -> None:
        self.tsr = TShirtRule(name="TShirt Discount")

    def tearDown(self) -> None:
        self.tsr = None

    def tshirt_list_generator(self, q:int) -> List[Product]:
        """Generates a list of q tshirts"""

        tshirt_list: List[Product] = []
        for _ in range(q):
            tshirt = Product(code=Code.TSHIRT, name="Summer T-Shirt", price=20.0)
            tshirt_list.append(tshirt)
        return tshirt_list

    def test_zero_tshirt(self) -> None:
        """Tests that no discount is applied with zero tshirts"""

        if self.tsr is None:
            self.fail("TShirt rule should not be None")

        self.assertEqual(self.tsr.get_discount(), None)

    def test_two_tshirt(self) -> None: 
        """Tests that no discount is applied with two tshirts"""

        if self.tsr is None:
            self.fail("TShirt rule should not be None")

        products = self.tshirt_list_generator(2)
        for product in products:
            self.tsr.scan(product)

        self.assertEqual(self.tsr.get_discount(), None)
    
    def test_three_tshirt(self) -> None: 
        """Tests that the discount is applied with three tshirts"""

        if self.tsr is None:
            self.fail("TShirt rule should not be None")

        products = self.tshirt_list_generator(3)
        for product in products:
            self.tsr.scan(product)

        discount: Optional[Discount] = self.tsr.get_discount()

        if discount is None:
            self.fail("Discount should not be None")

        self.assertAlmostEqual(discount.discount, 3.0)

    def test_four_tshirt(self) -> None: 
        """Tests that the discount is applied with four tshirts"""

        if self.tsr is None:
            self.fail("TShirt rule should not be None")

        products = self.tshirt_list_generator(4)
        for product in products:
            self.tsr.scan(product)

        discount: Optional[Discount] = self.tsr.get_discount()

        if discount is None:
            self.fail("Discount should not be None")

        self.assertAlmostEqual(discount.discount, 4.0)

if __name__ == '__main__':
    unittest.main()