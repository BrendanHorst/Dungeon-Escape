class Player(object):

    def __init__(self):

        self.jail_key = False
        self.jetpack = False
        self.angered_void = False
        self.cursed = False
        self.prompt = "(Dungeons) > "

    def die(self):

        print("-----YOU DIED!-----")
        return 'dead'
