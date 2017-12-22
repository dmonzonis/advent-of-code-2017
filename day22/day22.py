from collections import defaultdict


class Grid:
    def __init__(self, sgrid):
        self.infected = defaultdict(bool)

        sgrid = sgrid.splitlines()
        for y in range(len(sgrid)):
            for x in range(len(sgrid[y])):
                if sgrid[y][x] == '#':
                    self.infected[(x, y)] = True

        self.origin = (len(sgrid[0]) // 2, len(sgrid) // 2)


class Virus:
    def __init__(self, grid):
        self.grid = grid
        self.pos = grid.origin
        self.direction = (0, -1)
        self.total_infections = 0

    def turn_left(self):
        self.direction = (self.direction[1], -self.direction[0])

    def turn_right(self):
        self.direction = (-self.direction[1], self.direction[0])

    def move(self):
        self.pos = tuple([sum(x) for x in zip(self.pos, self.direction)])

    def infection_step(self):
        if self.grid.infected[self.pos]:
            self.turn_right()
        else:
            self.turn_left()
            self.total_infections += 1
        self.grid.infected[self.pos] = not self.grid.infected[self.pos]
        self.move()


def main():
    with open("input") as f:
        inp = f.read()

    grid = Grid(inp)
    virus = Virus(grid)

    for _ in range(10000):
        virus.infection_step()

    print("Part 1:", virus.total_infections)



if __name__ == "__main__":
    main()
