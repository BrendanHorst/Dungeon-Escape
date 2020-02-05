import rooms

class Map(object):

    def __init__(self):

        self.room_1 = rooms.Room1()
        self.room_2 = rooms.Room2()

    def next_room(self, target):

        return getattr(self, target).enter()
