from math import sqrt, ceil, floor
from collections import defaultdict
from enum import Enum


class Direction(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3


class Spiral:
    def __init__(self):
        self._grid = defaultdict(dict)
        self._grid[0][0] = 1  # Initial value at coordinate (0, 0)

    def get(self, position):
        x, y = position
        if x not in self._grid or y not in self._grid[x]:
            return 0
        return self._grid[x][y]

    def put(self, position, value):
        x, y = position
        self._grid[x][y] = value

    def generate(self, n):
        """
        Generates the sum spiral up to a value n and returns the value of the last element
        in the spiral
        """
        # Make new spiral
        self.__init__()

        x, y = 0, 0  # Coordinates
        dir = Direction.RIGHT  # Movement direction
        length = 0  # Max segment length at current ring
        elem = 1  # Element of the spiral, sum of adjacent values

        while elem <= n:
            if dir == Direction.UP:
                if y < length:
                    # Move up
                    y += 1
                else:
                    # Turn left
                    x -= 1
                    dir = Direction.LEFT
            elif dir == Direction.LEFT:
                if x > -length:
                    # Move left
                    x -= 1
                else:
                    # Turn down
                    y -= 1
                    dir = Direction.DOWN
            elif dir == Direction.DOWN:
                if y > -length:
                    # Move down
                    y -= 1
                else:
                    # Turn right
                    x += 1
                    dir = Direction.RIGHT
            elif dir == Direction.RIGHT:
                if x < length:
                    # Move right
                    x += 1
                else:
                    # Turn up and update length
                    y += 1
                    dir = Direction.UP
                    length += 1

            elem = 0
            # Sum elements in every adjacent direction
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    x_adj = x + dx
                    y_adj = y + dy
                    elem += self.get((x_adj, y_adj))

            # Put element in the spiral
            self.put((x, y), elem)

        return elem


def manhattan_distance(n):
    # Using the lower negative diagonal (which are just the squares of odd
    # numbers) we can get the ring number
    ring = floor(ceil(sqrt(n)) / 2)
    # Steps to reach nearest axis
    offset = (n - (2 * ring - 1)**2) % (2 * ring)
    # Going to the nearest axis and traveling back from rings gives us the distance
    return ring + abs(offset - ring)


def main():
    inp = 368078
    print("Part 1:", manhattan_distance(inp))
    spiral = Spiral()
    last = spiral.generate(inp)
    print("Part 2:", last)


if __name__ == "__main__":
    main()
