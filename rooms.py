import player

player = player.Player()

class Room(object):

    def __init__(self):

        self.adjacent_rooms = { 'north': None, 'east': None, 'south': None, 'west': None }

    def move(self, direction):

        print(f"You decide to move {direction}")

        return self.adjacent_rooms.get(direction)

# -----Dungeon Area-----

class Start(Room):

    def __init__(self):

        super(Start, self).__init__()

        self.adjacent_rooms['north'] = 'dungeon'

    def enter(self):

        print("\nYou look around inside the dilapidated cell.  The bars are rusted and bent all out of shape, and the door is nonexistant.  Up above you can see the hole you fell down; it's so narrow and tall that you can't see the top.  Other than the remains of a wooden bench there isn't anything else in the cell.")

        while True:

            print("What will you do?")
            print("1: Leave the cell")
            print("2: Try to go back up the hole")

            decision = input(player.prompt)

            if decision == '1':

                return self.move('north')

            if decision == '2':

                if player.jetpack == True:

                    print("You fly up the hole in the ceiling using the jetpack, but it's a tight fit.  Unfortunately, on the way up the jetpack's fuel supply strkes a rock and explodes.")
                    return player.die()

                else:

                    print("You try and jump up to the hole, however the ceiling is too high for you to reach.")


class Dungeon(Room):

    def __init__(self):

        super(Dungeon, self).__init__()

        self.adjacent_rooms['south'] = 'start'
        self.adjacent_rooms['north'] = 'north_cell'
        self.adjacent_rooms['east'] = 'east_cell'
        self.adjacent_rooms['west'] = 'crossroads'

    def enter(self):

        print("\nYou enter what appears to be the ruins of an ancient dungeon, with rubble everywhere.  There are only 3 cells accessible; anything else seems to have been cut off from a cave-in")

        while True:

            print("You can move north, south, east, or west \n1: North\n2: South\n3: East\n4: West")

            direction = input(player.prompt)

            if direction == '1':

                return self.move('north')

            elif direction == '2':

                return self.move('south')

            elif direction == '3':

                if player.jail_key == True:

                    print("With the key in had, the cell door opens without a hitch.")
                    return self.move('east')

                else:

                    print("You attempt to open the east cell door, but it is locked tight!")

            elif direction == '4':

                return self.move('west')


class North_Cell(Room):

    def __init__(self):

        super(North_Cell, self).__init__()

        self.adjacent_rooms['south'] = 'dungeon'

    def enter(self):

        print("\nThe door to the north cell opens without a problem.  You take two steps forward and the floor starts to give.  You quickly turn around to leave, but it's too late.  The floor below you collapses and you fall towards a pit of spikes, lava, sawblades, and sharks somehow.  Must be lava sharks.  You don't die to any of that, though, you hit a rock on your way down.")
        return player.die()


class East_Cell(Room):

    def __init__(self):

        super(East_Cell, self).__init__()

        self.adjacent_rooms['west'] = 'dungeon'

    def enter(self):

        print("\nYou enter the east cell.  There is a mysterious package hidden underneath the wooden bench.")

        while True:

            print("What will you do?")
            print("1: Leave the Cell")
            print("2: Open the package")

            decision = input(player.prompt)

            if decision == '1':

                return self.move('west')

            if decision == '2':

                if player.jetpack == False:

                    print("You carefully open up the package.  Inside it is a jetpack!  What luck!  It appears to be pretty old and fragile, but it could definitely help out.")
                    print("You obtained the jetpack!")
                    player.jetpack = True

                elif player.jetpack == True:

                    print("Unsatisfied with the jetpack, you reach back into the package for anything else, only to be greeted with an intense, sharp pain.  Inside the package is a strange looking scorpion, but before you can process it your whole body disintegrates into dust.")
                    return player.die()


# -----Cavern Area-----

class Crossroads(Room):

    def __init__(self):

        super(Crossroads, self).__init__()

        self.adjacent_rooms['east'] = 'dungeon'
        self.adjacent_rooms['west'] = 'bridge_east'
        self.adjacent_rooms['north'] = 'root_forest'

    def enter(self):

        player.prompt = "(Caverns) > "

        print("\nYou enter a large open cavern with crumbling stone brick paths showing the way.")

        while True:

            print('Where will you go?\n1: North\n2: East\n3: West')

            decision = input(player.prompt)

            if decision == '1':

                return self.move('north')

            elif decision == '2':

                return self.move('east')

            elif decision == '3':

                return self.move('west')


class Bridge_East(Room):

    def __init__(self):

        super(Bridge_East, self).__init__()

        self.adjacent_rooms['east'] = 'crossroads'
        self.adjacent_rooms['west'] = 'bridge_west'

    def enter(self):

        print("\nStanding before you is what seems to have once been a bridge, however all that remains is an impassable ravine stretching down into the abyss.")

        while True:

            print("What will you do?")
            print("1: Throw a rock into the ravine")
            print("2: Jump over the ravine (west)")
            print("3: Head east")

            decision = input(player.prompt)

            if decision == '1':

                print("You pick up the nearest stone and drop it over the edge.  The rock is swallowed by the darkness and never makes a sound.  Strangely, the air around you feels a bit colder and you feel a slight sense of dread.")
                player.angered_void = True

            elif decision == '2' and player.jetpack == False:

                print("I said the ravine was impassable, did I not?  You fall and die.  You idiot.")
                return player.die()

            elif decision == '2' and player.jetpack == True:

                print("You make a flying leap over the edge, and the jetpack kicks in and lifts you up.")

                if player.angered_void == True:

                    print("As you fly across, you feel the same sense of dread that you felt when throwing the stone down.  It feels as if... something is angry.  Suddenly, a mass of shadow rises up from the depths, and a tendril reached out and grabs you by the ankle.  It pulls you down into the abyss, but you were already dead the moment it touched you.")
                    return player.die()

                print("You fly across safely, and you can't help but let out a sigh of releif as your feet alight upon the other side.")

            elif decision == '3':

                return self.move('east')

class Bridge_West(Room):

    def __init__(self):

        super(Bridge_West, self).__init__()

        self.adjacent_rooms['east'] = 'bridge_east'
        self.adjacent_rooms['north'] = 'cavern_entrance'

    def enter(self):

        print("\nYou are on the western side of the destroyed bridge.")

        while True:

            print("Where will you go?")
            print("1: Head north")
            print("2: Fly across the ravine (east)")

            decision = input(player.prompt)

            if decision == '1':

                return self.move('north')

            if decision == '2':

                print("You fly back across the ravine using the jetpack")
                return self.move('east')

class Cavern_Entrance(Room):

    def __init__(self):

        super(Cavern_Entrance, self).__init__()

        self.adjacent_rooms['south'] = 'bridge_west'
        self.adjacent_rooms['north'] = 'goal'

    def enter(self):

        print("The cave starts to get wider and the air a little nicer as you walk.  Up ahead, a few beams of light appear from the other end of the cavern.  But in order to get to the exit, you need to get past the dragon.  And the dragon looks hungry.")

        while True:

            print("What will you do?")
            print("1: Fly over the dragon with the jetpack")
            print("2: Offer yourself to the dragon")
            print("3: Flee back to the south")

            decision = input(player.prompt)

            if decision == '1':

                print("You try to fly over the dragon, but the dragon merely breathes fire at you which makes the jetpack explode.")
                return player.die()

            elif decision == '2':

                print("You realize you have no hope of defeating a dragon with no weapons, so you give up and offer yourself to the dragon, hoping that maybe it'll spare you.")

                if player.cursed == False:

                    print("The dragon walks up to you, sniffs you to make sure you haven't consumed any cursed water, then devours you whole")
                    return player.die()

                elif player.cursed == True:

                    print("The dragon walks up to you and sniffs you.  He detects that you have cursed water within your body and decides against eating you for now.  You use this opportunity to head north towards the mouth of the cave")
                    return 'goal'

            elif decision == '3':

                return self.move('south')



# -----Overgown Area-----

class Root_Forest(Room):

    def __init__(self):

        super(Root_Forest, self).__init__()

        self.adjacent_rooms['south'] = 'crossroads'
        self.adjacent_rooms['west'] = 'waterfall'

    def enter(self):

        player.prompt = "(Overgrowth) > "

        print("\nYou enter a room filled with the roots from what must be a forest on the surface, so that it's hard to move around.")

        while True:

            print("What will you do?")
            print("1: Head north")
            print("2: Head south")
            print("3: Head east")
            print("4: Head west")

            decision = input(player.prompt)

            if decision == '1':

                print("You try to head north, and see a small passageway hidden behind the roots.  You work your way over to it only to see a pair of glowing eyes looking out the darkness back at you.  Before you have time to react, whatever it was grabs you and pulls you into its den.")
                return player.die()

            if decision == '2':

                return self.move('south')

            if decision == '3':

                print("You try to head east through the roots, only to hit a wall.")

                if player.jail_key == False:

                    print("However, you see a small glimmer on the ground.  You push some roots aside and grab what turns out to be a slightly rusted key.  This could come in handy.")
                    print("You obtained the rusty key!")
                    player.jail_key = True

            if decision == '4':

                return self.move('west')


class Waterfall(Room):

    def __init__(self):

        super(Waterfall, self).__init__()

        self.adjacent_rooms['east'] = 'root_forest'

    def enter(self):

        print("\nYou hit a dead end in a pretty room with a waterfall pouring into a small pool of clear water.  You realize that you are quite thirsty.")

        drink_count = 0;

        while True:

            print("What do you do?")
            print("1: Stop to take a drink")
            print("2: Head east")

            decision = input(player.prompt)

            if drink_count == 2:

                 decision = '1'

            if decision == '1':

                if drink_count == 0:

                    print("You decide to take a drink from the water.  It's delicious.  You feel compelled to drink it agian.")
                    drink_count = 1
                    player.cursed = True

                elif drink_count == 1:

                    print("The water is so good you gulp it down.  The water is cool.  The water is refreshing.  The water is all you need.")
                    drink_count = 2

                elif drink_count == 2:

                    print("You can't even make decisions anymore, all you can think of is drinking more water from the pool.  As you bend down to get another gulp, a beautiful water spirit materializes before your eyes and reaches her hand out to you.  Without thinking, you take it, and she abruptly pulls you under the water, which is a lot deeper than it looks from above.  You try to tell your body to wrestle free, but you've been cursed by the water and are completely helpless.  You accept your fate and drown.")
                    return player.die()

            if decision == '2':

                return self.move('east')



class Goal(Room):

    def enter(self):

        print("Congradulations, You escaped!")

        return('win')
