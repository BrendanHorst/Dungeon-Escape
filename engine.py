from map import map

class Engine(object):
    """Creates and engine object that runs the game until it is won or lost"""

    def __init__(self):
        """Initializes the engine objet with a map object and sets the starting room to 'start'"""

        self.map = Map()
        self.room = 'start' #Next room to be entered

    def play(self):
        """Starts the game, continues to enter the next room until the game is either won or lost"""

        print("You wake up in what seems to be the ruins of an old underground dungeon.  Just a few hours ago you fell down a hole in the woods, somehow survived, and ended up here.  You don't remember ever learning about these ruins, but all that matters now is finding a way out.")

        while self.room != 'win' and self.room != 'dead':

            #Goes to the next room (as defined by self.room), then stores the next room after that
            self.room = self.map.next_room(self.room)
