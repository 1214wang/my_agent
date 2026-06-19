import unittest
from shopping_list import ShoppingList
class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shoppinglist=ShoppingList({"鞋子":30,"书":12,"衣服":43})
    def test_get_item_count(self):
        # shoppinglist=ShoppingList({"鞋子":30,"书":12,"衣服":43})
        self.assertEqual(self.shoppinglist.get_item_count(),3)
    def test_get_total_price(self):
        # shoppinglist=ShoppingList({"鞋子":30,"书":12,"衣服":43})
        self.assertEqual(self.shoppinglist.get_total_price(),85)