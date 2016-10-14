# author: Hendrik Werner // s4549775
# author: Jasper Haasdijk // s4449754
# author: Jelle Loman // s4573382

import random
import statistics

class Game:
    def __init__(self, distance):
        self.distance = distance
        self.max_distance = distance

    def play(self):
        while self.distance and self.distance <= self.max_distance:
            self._throw()
        return 0 if self.distance else 1


    def _throw(self):
        if random.randrange(0, 2):
            self.distance -= 1
        else:
            self.distance += 1

if __name__ == "__main__":
    n = 100
    tries = 10000
    chance = 1 / 6
    print(
        chance - (
            statistics.mean(
                [sum([Game(5).play() for i in range(n)]) for j in range(tries)]
            ) / n
        )
    )
