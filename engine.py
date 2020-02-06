import map

class Engine(object):

    def __init__(self):

        self.map = map.Map()
        self.room = 'start'

    def play(self):

        print("You wake up in what seems to be the ruins of an old underground dungeon.  Just a few hours ago you fell down a hole in the woods, somehow survived, and ended up here.  You don't remember ever learning about these ruins, but all that matters now is finding a way out.")

        while self.room != 'win' and self.room != 'dead':

            self.room = self.map.next_room(self.room)
