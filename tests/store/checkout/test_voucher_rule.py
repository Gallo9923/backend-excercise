import unittest

from store.checkout.pricing_rule import VoucherRule
from store.checkout.product import Product

class VoucherRuleTestCase(unittest.TestCase):

    vr_name: str = "Voucher Rule"
    vr: VoucherRule = None

    def setUp(self) -> None:
        self.vr = VoucherRule(name=self.vr_name)

    def tearDown(self) -> None:
        self.vr = None
    
    def test_VoucherRule(self) -> None:
        """Test if the the voucher rule is created successfully"""
        self.assertEqual(self.vr.name, self.vr_name)
        self.assertEqual(self.vr.voucher_counter, 0)

    def test_one_voucher_items(self) -> None:
        """Test if the voucher discount is applied for one voucher items"""
        pass

    def test_two_voucher_items(self) -> None:
        """Test if the voucher discount is applied for two voucher items"""

        pass

    def test_three_voucher_items(self) -> None:
        """Test if the voucher discount is applied for three voucher items"""
        pass


if __name__ == '__main__':
    unittest.main()