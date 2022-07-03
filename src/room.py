class Room:
    def __init__(self, _room_num, _max_capacity):
        self.room_num = _room_num
        self.max_capacity = _max_capacity
        self.list_of_guests = []
        self.till = 0
        self.list_of_songs = {}

    
    def check_guest_in(self, guest):
        self.list_of_guests.append(guest)
    
    def check_guest_out(self, guest):
        self.list_of_guests.remove(guest)

    def add_song(self, song):
        self.list_of_songs[song.name] = song