class Room(object):

    def __init__(self):

        self.adjacent_rooms = { 'north': None, 'east': None, 'south': None, 'west': None }

    def move(self, direction):

        print(f"You decide to move {direction}")

        return self.adjacent_rooms.get(direction)


class Start(Room):

    def enter(self, player):

        self.adjacent_rooms['north'] = 'dungeon'

        print("You are in the first room")

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


class Goal(Room):

    def enter(self, player):

        print("You escaped!")

        return('win')
