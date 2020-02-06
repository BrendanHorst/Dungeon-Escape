class Room(object):

    def __init__(self):

        self.adjacent_rooms = { 'north': None, 'east': None, 'south': None, 'west': None }

    def move(self, direction):

        print(f"You decide to move {direction}")

        return self.adjacent_rooms.get(direction)

# -----Dungeon Area-----

class Start(Room):

    def enter(self, player):

        self.adjacent_rooms['north'] = 'dungeon'

        print("The cell is empty aside ")

        input()

        return self.move('north')


class Dungeon(Room):

    def enter(self, player):

        self.adjacent_rooms['south'] = 'start'
        self.adjacent_rooms['north'] = 'north_cell'
        self.adjacent_rooms['east'] = 'east_cell'
        self.adjacent_rooms['west'] = 'crossroads'

        print("You are in the second room")

        while True:

            print("You can move north, south, east, or west \n1: North\n2: South\n3: East\n4: West")

            direction = input(player.prompt)

            if direction == '1':
                return self.move('north')
            elif direction == '2':
                return self.move('south')
            elif direction == '3':
                if player.jail_key == True:
                    return self.move('east')
                else:
                    print("You attempt to open the cell door, but it is locked tight!")
            elif direction == '4':
                return self.move('west')


class North_Cell(Room):

    def enter(self, player):

        self.adjacent_rooms['south'] = 'dungeon'

        return self.move('south')


class East_Cell(Room):

    def enter(self, player):

        self.adjacent_rooms['west'] = 'dungeon'

        return self.move('west')


# -----Cavern Area-----

class Crossroads(Room):

    def enter(self, player):

        self.adjacent_rooms['east'] = 'dungeon'
        self.adjacent_rooms['west'] = 'bridge_east'
        self.adjacent_rooms['north'] = 'root_forest'

        input(player.prompt)

        return self.move('east')


class Bridge_East(Room):

    def enter(self, player):

        self.adjacent_rooms['east'] = 'crossroads'
        self.adjacent_rooms['west'] = 'bridge_west'

        print("Standing before you is what seems to have once been a bridge, however all that remains is an impassable ravine stretching down into the abyss.")

        while True:

            print("What will you do?")
            print("1: Throw a rock into the ravine")
            print("2: Jump over the ravine (west)")
            print("3: Head east")

            decision = input(player.prompt)

            if decision == '1':
                print("You pick up the nearest stone and drop it over the edge.  The rock is swallowed by the darkness and never makes a sound.  Strangely, the air around you feels a bit colder and you feel a slight sense of dread.")
                player.bad_karma = True
            elif decision == '2' and player.jetpack == False:
                print("I said the ravine was impassable, did I not?  You fall and die.  You idiot.")
                #death
            elif decision == '2' and player.jetpack == True:
                pass
            elif decision == '3':
                return self.move('east')

class Bridge_West(Room):

    def enter(self, player):

        self.adjacent_rooms['east'] = 'bridge_east'

class Cavern_Entrance(Room):

    def enter(self, player):

        self.adjacent_rooms['south'] = 'bridge_west'
        self.adjacent_rooms['north'] = 'goal'



# -----Overgown Area-----

class Root_Forest(Room):

    def enter(self, player):

        self.adjacent_rooms['south'] = 'crossroads'
        self.adjacent_rooms['west'] = 'waterfall'


class Waterfall(Room):

    def enter(self, player):

        self.adjacent_rooms['east'] = 'root_forest'



class Goal(Room):

    def enter(self, player):

        print("You escaped!")

        return('win')
