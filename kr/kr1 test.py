import unittest
from kr1 import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item('Apple', 0.5, 3)
        self.cart.add_item('Banana', 0.3, 5)
        self.assertEqual(len(self.cart), 2)
        expected_str = "Кошик покупок:\nApple: 3 шт. по 0.50 грн\nBanana: 5 шт. по 0.30 грн\nЗагальна вартість: 3.00 грн"
        self.assertEqual(str(self.cart), expected_str)
        self.assertEqual(self.cart.total_cost, 3.00)

    def test_add_existing_item(self):
        self.cart.add_item('Apple', 0.5, 3)
        self.cart.add_item('Apple', 0.5, 2)
        expected_str = "Кошик покупок:\nApple: 5 шт. по 0.50 грн\nЗагальна вартість: 2.50 грн"
        self.assertEqual(str(self.cart), expected_str)
        self.assertEqual(self.cart.total_cost, 2.5)

    def test_add_item_with_different_prices(self):
        self.cart.add_item('Apple', 0.5, 3)
        self.cart.add_item('Apple', 0.1, 2)
        expected_str = "Кошик покупок:\nApple: 3 шт. по 0.50 грн\nApple: 2 шт. по 0.10 грн\nЗагальна вартість: 1.70 грн"
        self.assertEqual(str(self.cart), expected_str)
        self.assertEqual(self.cart.total_cost, 1.7)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            self.cart.add_item('Apple', -0.5, 3)

    def test_zero_price(self):
        with self.assertRaises(ValueError):
            self.cart.add_item('Apple', 0, 3)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add_item('Apple', 0.5, -3)

    def test_zero_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add_item('Apple', 0.5, 0)

if __name__ == '__main__':
    unittest.main()
