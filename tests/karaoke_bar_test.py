import unittest
from src.karaoke_bar import KaraokeBar
from src.room import Room
from src.guest import Guest

class TestKaraokeBar(unittest.TestCase):

    def setUp(self):
        self.karaoke_bar = KaraokeBar("The Empty Ocestra", 2)
        self.room1 = Room("1", 5)
        self.room2 = Room("2", 3)
        self.guest1 = Guest("Sam", 100, "Yesterday")
        self.guest2 = Guest("Benjamin", 70, "Dancing Queen")
        self.guest3 = Guest("Lewis", 60, "Some song")
        self.guest4 = Guest("Jack", 60, "Some song")

    def test_karaoke_bar_is_set_up_properly(self):
        self.assertEqual("The Empty Ocestra", self.karaoke_bar.name)
        self.assertEqual(2, self.karaoke_bar.num_of_rooms)

    def test_room_takes_guests_in(self):
        self.karaoke_bar.add_room(self.room1)
        self.karaoke_bar.room_guest_check_in(self.guest1)
        self.assertEqual(1, len(self.room1.list_of_guests))
    
    def test_check_room_added_to_bar(self):
        self.karaoke_bar.add_room(self.room1)
        self.assertEqual(1, len(self.karaoke_bar.room))
    
    def test_check_room2_is_full(self):
        self.karaoke_bar.add_room(self.room2)
        self.karaoke_bar.add_room(self.room1)
        self.karaoke_bar.room_guest_check_in(self.guest1)
        self.karaoke_bar.room_guest_check_in(self.guest2)
        self.karaoke_bar.room_guest_check_in(self.guest3)
        self.karaoke_bar.room_guest_check_in(self.guest4)
        self.assertEqual(3, len(self.room2.list_of_guests))
        self.assertEqual(1, len(self.room1.list_of_guests))
    
    def test_guests_pay_for_entry(self):
        self.karaoke_bar.add_room(self.room2)
        self.karaoke_bar.room_guest_check_in(self.guest1)
        self.karaoke_bar.room_guest_check_in(self.guest2)
        self.assertEqual(20, self.karaoke_bar.till)