# author: Hendrik Werner // s4549775
# author: Jasper Haasdijk // s4449754
# author: Jelle Loman // s4573382

import random
import statistics


class Game:
    def __init__(self, distance, visualize=False):
        self.distance = distance
        self.max_distance = distance
        self.visualize = visualize

    def play(self):
        self._visualize()
        while self.distance and self.distance <= self.max_distance:
            self._throw()
            self._visualize()
        return 0 if self.distance else 1

    def _visualize(self):
        if self.visualize:
            print(self)

    def _throw(self):
        if random.randrange(0, 2):
            self.distance -= 1
        else:
            self.distance += 1

    def __str__(self):
        if self.distance:
            if self.distance <= self.max_distance:
                return "M" \
                       + (self.distance - 1) * "_" \
                       + "K" \
                       + (self.max_distance - self.distance) * "_" \
                       + "W"
            else:
                return "Failed"
        else:
            return "Solved"


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
