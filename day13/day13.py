class Firewall:
    def __init__(self, inp):
        self.state = {}
        parsed = parse_input(inp)
        for depth, max_range in parsed:
            # Initially, all scanners are at position 0 (top), and start moving down
            self.state[depth] = {'position': 0, 'range': max_range, 'direction': 1}

    def update(self):
        """Move scanners on every depth layer one step."""
        for depth in self.state.keys():
            # Change direction if needed
            if (self.state[depth]['position'] == self.state[depth]['range'] - 1 and
                    self.state[depth]['direction'] == 1):
                self.state[depth]['direction'] = -1
            elif self.state[depth]['position'] == 0 and self.state[depth]['direction'] == -1:
                self.state[depth]['direction'] = 1

            # Move
            self.state[depth]['position'] += self.state[depth]['direction']

    def check_scanner(self, depth, pos):
        """Check if there is a scanner at given depth and position."""
        if depth not in self.state:
            return False
        return self.state[depth]['position'] == pos

    def severity(self, depth):
        """Return the severity of getting caught at a given depth."""
        return depth * self.state[depth]['range']


def parse_input(inp):
    """Parse input and return a list of tuples containing depth and range."""
    return [(int(d), int(r)) for d, r in [line.split(': ') for line in inp.splitlines()]]


def packet_travel(firewall):
    """Send a packet through a firewall and returns the total severity of the trip."""
    severity = 0
    final_depth = max(firewall.state.keys())
    for depth in range(final_depth + 1):
        if firewall.check_scanner(depth, 0):
            severity += firewall.severity(depth)
        firewall.update()
    return severity


def main():
    with open("input") as f:
        inp = f.read().strip()

    firewall = Firewall(inp)
    print("Part 1:", packet_travel(firewall))


if __name__ == "__main__":
    main()
