import unittest

from shop.pricing import apply_discount, cart_total


class InvertedDiscountRegression(unittest.TestCase):
    """Issue #1: a discount must lower the price by that percentage."""

    def test_ten_percent_off(self):
        self.assertEqual(apply_discount(200.0, 10), 180.0)

    def test_cart_total_with_discount(self):
        self.assertEqual(cart_total([(50.0, 2)], discount=10), 90.0)


if __name__ == "__main__":
    unittest.main()
