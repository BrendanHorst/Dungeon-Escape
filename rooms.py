class Room(object):

    def __init__(self):

        self.adjacent_rooms = { 'north': None, 'east': None, 'south': None, 'west': None }

    def move(self, direction):

        print(f"You decide to move {direction}")

        print(self.adjacent_rooms[direction])

        return self.adjacent_rooms.get(direction)

class Room1(Room):

    def enter(self):

        self.adjacent_rooms['north'] = 'room_2'

        print("You are in the first room")

        input()

        return self.move('north')

class Room2(Room):

    def enter(self):

        self.adjacent_rooms['south'] = 'room_1'
        self.adjacent_rooms['north'] = 'goal_room'

        print("You are in the second room")

        print("You can move north or south \n1: North\n2: South")

        direction = input("> ")

        if direction == '1':
            return self.move('north')
        elif direction == '2':
            return self.move('south')

class Goal(Room):

    def enter(self):

        print("You escaped!")

        return('win')
