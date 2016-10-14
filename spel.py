import random

class Game:
    def __init__(self, distance):
        self.distance = distance
        self.max_distance = distance

    def play(self):
        while self.distance and self.distance <= self.max_distance:
            self._throw()
        return self.distance == 0


    def _throw(self):
        if random.randrange(0, 2):
            self.distance -= 1
        else:
            self.distance += 1

if __name__ == "__main__":
    print(Game(5).play())
