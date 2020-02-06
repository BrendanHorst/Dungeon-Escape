class Player(object):

    def __init__(self):

        self.jail_key = False
        self.jetpack = False
        self.location = 'Dungeons'
        self.prompt = f"({self.location}) > "
