import unittest
from typing import List, Optional
from src.store.checkout.discount import Discount

from src.store.checkout.pricing_rule import VoucherRule
from src.store.checkout.product import Product, Code

class VoucherRuleTestCase(unittest.TestCase):

    vr_name: str = "Voucher Rule"
    vr: Optional[VoucherRule] = None

    def setUp(self) -> None:
        self.vr = VoucherRule(name=self.vr_name)

    def tearDown(self) -> None:
        self.vr = None # type: ignore
    
    def test_voucher_rule(self) -> None:
        """Tests if the the voucher rule is created successfully"""

        if self.vr is None:
            self.fail("Voucher rule should not be None")

        self.assertEqual(self.vr.name, self.vr_name)
        self.assertEqual(self.vr.voucher_counter, 0)

    def test_scan_counter(self) -> None: 
        """Tests whether the voucher rule is couting voucher type products"""

        if self.vr is None:
            self.fail("Voucher rule should not be None")

        p: Product = Product(code=Code.VOUCHER, name="Gift Card", price=5.0)
        self.vr.scan(p)

        self.assertEqual(self.vr.voucher_counter, 1)  

    def test_zero_voucher_items(self) -> None:
        """Tests that no discount is applied with zero voucher items"""

        if self.vr is None:
            self.fail("Voucher rule should not be None")

        p = Product(code=Code.PANTS, name="Summer Pants", price=7.5)
        self.vr.scan(p)

        self.assertEqual(self.vr.get_discount(), None)
        

    def voucher_list_generator(self, q: int) -> List[Product]:
        """Generates  a list of q voucher products"""

        voucher_list: List[Product] = []
        for _ in range(q):
            p: Product = Product(code=Code.VOUCHER, name="Gift Card", price=5.0)
            voucher_list.append(p)
        return voucher_list

    def test_one_voucher_items(self) -> None:
        """Tests if the voucher discount is applied for one voucher items"""
        
        if self.vr is None:
            self.fail("Voucher rule should not be None")

        products: List[Product] = self.voucher_list_generator(1)
        for p in products:
            self.vr.scan(p)

        self.assertEqual(self.vr.get_discount(), None)

    def test_two_voucher_items(self) -> None:
        """Test if the voucher discount is applied for two voucher items"""
        
        if self.vr is None:
            self.fail("Voucher rule should not be None")

        products: List[Product] = self.voucher_list_generator(2)
        for p in products:
            self.vr.scan(p)

        discount: Optional[Discount] = self.vr.get_discount()
        
        if discount is None:
            self.fail("Discount should not be none")
        
        self.assertAlmostEqual(discount.discount, 5.0)

    def test_three_voucher_items(self) -> None:
        """Test if the voucher discount is applied for three voucher items"""
        
        if self.vr is None:
            self.fail("Voucher rule should not be None")

        products: List[Product] = self.voucher_list_generator(3)
        for p in products:
            self.vr.scan(p)

        discount: Optional[Discount] = self.vr.get_discount()

        if discount is None: 
            self.fail("Discount should not be None")

        self.assertAlmostEqual(discount.discount, 5.0)


if __name__ == '__main__':
    unittest.main()