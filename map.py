import rooms
import player

player = player.Player()

class Map(object):

    def __init__(self):

        #Dungeon Area
        self.start = rooms.Start()
        self.dungeon = rooms.Dungeon()
        self.north_cell = rooms.North_Cell()
        self.east_cell = rooms.East_Cell()
        #Cavern Area
        self.crossroads = rooms.Crossroads()
        self.bridge_east = rooms.Bridge_East()
        self.bridge_west = rooms.Bridge_West()
        self.cavern_entrance = rooms.Cavern_Entrance()
        #Overgrown Area
        self.root_forest = rooms.Root_Forest()
        self.waterfall = rooms.Waterfall()

        self.goal = rooms.Goal()

    def next_room(self, target):

        return getattr(self, target).enter(player)
