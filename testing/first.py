import unittest
from testing.new import Operations
from classes.Item import *
from interfaces.order import *


class MyTest(unittest.TestCase):
    item = Item()
    def test_add_item(self):
        result = self.item.add_item('a', 'test_type',"110")
        self.assertTrue(result)

    def test_add_item1(self):
        result = self.item.add_item('', 'test_type',"100")
        self.assertFalse(result)

    def test_add_item2(self):
        result = self.item.add_item('', '',"")
        self.assertFalse(result)

    def test_add_item3(self):
        result = self.item.add_item("hello", "chicken","aaa")
        self.assertFalse(result)

    def test_add_item4(self):
        result = self.item.add_item("aa", 15,"100")
        self.assertFalse(result)

    def test_add_item5(self):
        result = self.item.add_item(10, "bb", "100")
        self.assertFalse(result)

    def test_showitem(self):
        obj=Item()
        result = obj.show_item()
        res=len(result)
        exp=31
        self.assertEqual(res,exp)

    def test_showitem1(self):
        obj=Item()
        result = obj.show_item()
        res=len(result)
        exp=32
        self.assertEqual(res,exp)

    def test_search(self):
        obj=Item()
        result = obj.search_item("chowmin")
        res=len(result)
        exp=0
        self.assertEqual(res,exp)

    def test_search1(self):
        obj=Item()
        result = obj.search_item("")
        self.assertFalse(result)

    def test_update(self):
        obj=Item()
        result = obj.update_item(10,"Pizza","Large","600")
        self.assertTrue(result)

    def test_update1(self):
        obj=Item()
        result = obj.update_item("","Pizza","Large","600")
        self.assertFalse(result)

    def test_delete(self):
        obj=Item()
        result = obj.delete_item(30)
        self.assertTrue(result)

    def test_delete1(self):
        obj=Item()
        result = obj.delete_item("")
        self.assertFalse(result)

    def test_add_order(self):
        obj=Order()
        result=obj.add_order(5,[("momo","veg",100)])
        self.assertTrue(result)

    def test_add_order1(self):
        obj=Order()
        result=obj.add_order_to_prev_customer([("momo","veg",100)],4)
        self.assertTrue(result)

    def test_show_order(self):
        obj=Order()
        result=obj.show_all_orders()
        mres=len(result)
        exp=9
        self.assertEqual(mres,exp)

