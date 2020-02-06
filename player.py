class Player(object):
    """Creates a player object that contains various attributes that affect the game and can die"""

    def __init__(self):
        """Initializes the player object with attributes that affect progression"""

        self.jail_key = False
        self.jetpack = False
        self.angered_void = False
        self.cursed = False
        self.prompt = "(Dungeons) > "

    def die(self):
        """Returns the string of 'dead', which will end the while loop in the engine"""

        print("-----YOU DIED!-----")
        return 'dead'
