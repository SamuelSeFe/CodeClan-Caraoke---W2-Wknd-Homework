import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Sam", 100, "Yesterday")
        self.guest2 = Guest("Jack", 5, "Some song")

    def test_guest_has_been_set_up_properly(self):    
        self.assertEqual("Sam", self.guest1.name)
        self.assertEqual(100, self.guest1.wallet)
        self.assertEqual("Yesterday", self.guest1.fav_song)
    
    def test_guest_has_enough_cash(self):
        self.guest1.check_wallet(5)
        self.assertEqual(True, self.guest1.check_wallet(5))
    
    def test_guest_doe_not_have_money(self):
        self.guest2.check_wallet(10)
        self.assertEqual(False, self.guest2.check_wallet(10))

    def test_remove_money_from_wallet(self):
        self.guest1.remove_money_from_wallet(10)
        self.assertEqual(90, self.guest1.wallet)
    
