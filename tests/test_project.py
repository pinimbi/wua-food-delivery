import unittest
from backend.auth import register_user, login_user
from backend.menu import get_menu
from backend.order import Order, update_order_status, get_order

class ProjectTests(unittest.TestCase):
    def test_register_login_and_password_safety(self):
        user=register_user("A Student", "a.student@example.edu", "WUA1", "strongpass")
        self.assertEqual(user["student_id"], "WUA1")
        self.assertNotIn("password", user)
        self.assertEqual(login_user("A.STUDENT@example.edu", "strongpass")["name"], "A Student")
        self.assertIsNone(login_user("a.student@example.edu", "wrongpass"))
    def test_register_rejects_bad_email_and_short_password(self):
        for args in [("X", "bad", "1", "longenough"), ("X", "x@y.org", "2", "short")]:
            with self.assertRaises(ValueError): register_user(*args)
    def test_menu_copy_and_unknown_cafe(self):
        menu=get_menu("Main Cafeteria")
        self.assertGreaterEqual(len(menu), 5)
        menu.clear()
        self.assertEqual(len(get_menu("Main Cafeteria")), 5)
        self.assertEqual(get_menu("Unknown"), [])
    def test_order_total_and_status(self):
        o=Order.create("WUA2", [{"id":"rice","name":"Rice","price":4.5,"quantity":2}])
        self.assertEqual(o.total_price, 9.0)
        self.assertEqual(update_order_status(o.order_id,"preparing").status,"preparing")
        self.assertEqual(get_order(o.order_id).status,"preparing")
    def test_order_rejects_invalid_items_and_status(self):
        with self.assertRaises(ValueError): Order.create("WUA3", [])
        o=Order.create("WUA4", [{"id":"water","name":"Water","price":.5}])
        with self.assertRaises(ValueError): update_order_status(o.order_id,"teleported")

if __name__ == "__main__": unittest.main()