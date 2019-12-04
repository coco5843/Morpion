class Player:

    def __init__(self, name):
        self.name = name
        self.counter = 0
        self.symbol = None
        self.positions = []

    def add_counter(self):
        self.counter += 1


