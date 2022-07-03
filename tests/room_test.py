import unittest
from src.room import Room
from src.guest import Guest
from src.songs import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("1", 5)
        self.room2 = Room("2", 3)
        self.guest1 = Guest("Sam", 100, "Yesterday")
        self.song1 = Song("Yesterday", "The Beatels", 2.03)
        self.song2 = Song("Dancing Queen", "ABBA", 3.53)
    
    def test_room_has_been_set_up_properly(self):
        self.assertEqual("1", self.room1.room_num)
        self.assertEqual(5, self.room1.max_capacity)
        self.assertEqual("2" , self.room2.room_num)
        self.assertEqual(3 , self.room2.max_capacity)
    
    def test_hidden_properties_of_room(self):
        self.assertEqual(0 ,self.room1.till)
        self.assertEqual(0, len(self.room1.list_of_songs))

    def test_check_guests(self):
        self.assertEqual(0, len(self.room1.list_of_guests))

    def test_check_guest_in(self):
        self.room1.check_guest_in(self.guest1)
        self.assertEqual(1, len(self.room1.list_of_guests))

    def test_check_guest_out(self):
        self.room1.check_guest_in(self.guest1)
        self.assertEqual(1, len(self.room1.list_of_guests))
        self.room1.check_guest_out(self.guest1)
        self.assertEqual(0, len(self.room1.list_of_guests))

    def test_check_list_of_songs_in_room(self):
        self.assertEqual(0, len(self.room1.list_of_songs))
        self.assertEqual(0, len(self.room2.list_of_guests))
    
    def test_add_song_dicitonary(self):
        self.room1.add_song(self.song1)
        self.room2.add_song(self.song2)
        self.assertEqual(1, len(self.room1.list_of_songs))
        self.assertEqual(1, len(self.room2.list_of_songs))
