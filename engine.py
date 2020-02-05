import map

class Engine(object):

    def __init__(self):

        self.map = map.Map()
        self.room = 'room_1'

    def play(self):

        self.room = self.map.next_room(self.room)
        self.room = self.map.next_room(self.room)
