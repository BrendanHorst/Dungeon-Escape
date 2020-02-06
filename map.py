import rooms
import player

player = player.Player()

class Map(object):

    def __init__(self):

        self.start = rooms.Start()
        self.dungeon = rooms.Dungeon()
        self.north_cell = rooms.North_Cell()
        self.east_cell = rooms.East_Cell()
        self.goal_room = rooms.Goal()

    def next_room(self, target):

        return getattr(self, target).enter(player)
