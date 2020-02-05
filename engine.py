import map

class Engine(object):

    def __init__(self):

        self.map = map.Map()
        self.room = 'room_1'

    def play(self):

        while self.room != 'win':

            self.room = self.map.next_room(self.room)
