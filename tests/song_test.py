import unittest
from src.songs import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Yesterday", "The Beatles", 2.03)

    def test_song_has_been_set_up_properly(self):
        self.assertEqual("Yesterday", self.song1.name)
        self.assertEqual("The Beatles", self.song1.artist_name)
        self.assertEqual(2.03, self.song1.length_of_song)
