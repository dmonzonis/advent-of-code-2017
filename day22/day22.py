from collections import defaultdict


class Grid:
    def __init__(self, sgrid):
        # 0 -> clean, 1 -> weakened, 2 -> infected, 3 -> flagged
        self.states = defaultdict(int)

        sgrid = sgrid.splitlines()
        for y in range(len(sgrid)):
            for x in range(len(sgrid[y])):
                if sgrid[y][x] == '#':
                    self.states[(x, y)] = 2

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

    def infection_step(self, flags=False):
        status = self.grid.states[self.pos]
        if status == 0:
            self.turn_left()
            if not flags:
                self.total_infections += 1
        elif status == 1:
            self.total_infections += 1
        elif status == 2:
            self.turn_right()
        else:
            self.turn_right()
            self.turn_right()

        if flags:
            self.grid.states[self.pos] = (status + 1) % 4
        else:
            self.grid.states[self.pos] = (status + 2) % 4

        self.move()


def main():
    with open("input") as f:
        inp = f.read()

    grid = Grid(inp)
    virus = Virus(grid)

    for _ in range(10000):
        virus.infection_step()

    print("Part 1:", virus.total_infections)

    grid = Grid(inp)
    virus = Virus(grid)

    for _ in range(10000000):
        virus.infection_step(flags=True)

    print("Part 2:", virus.total_infections)


if __name__ == "__main__":
    main()
