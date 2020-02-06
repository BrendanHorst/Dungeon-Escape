from rooms import rooms

class Map(object):
    """Creates a map object that stores all of the room objects and enters them"""

    def __init__(self):
        """Initializes the map with objects for every Room class"""

        #Dungeon Area
        self.start = Start()
        self.dungeon = Dungeon()
        self.north_cell = NorthCell()
        self.east_cell = EastCell()
        #Cavern Area
        self.crossroads = Crossroads()
        self.bridge_east = BridgeEast()
        self.bridge_west = BridgeWest()
        self.cavern_entrance = CavernEntrance()
        #Overgrown Area
        self.root_forest = RootForest()
        self.waterfall = Waterfall()

        self.goal = Goal()

    def next_room(self, target):
        """Takes a string that should correspond with one of the map's room objects,
        calls the enter method on that object, then returns what the room object returns.
        Which is also a string that is the name of another room object"""

        return getattr(self, target).enter()
