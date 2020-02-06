class Player(object):

    def __init__(self):

        self.jail_key = False
        self.jetpack = False
        self.bad_karma = False
        self.prompt = "> "

    def die(self):

        print("-----YOU DIED!-----")
        return 'dead'
