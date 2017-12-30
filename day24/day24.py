class Bridge:
    """Represents a bridge of magnetic pieces.

    Holds information about available pieces to construct the bridge, current pieces used
    in the bridge and the available port of the last piece in the bridge."""

    def __init__(self, available, bridge=[], port=0):
        """Initialize bridge variables."""
        self.available = available
        self.bridge = bridge
        self.port = port

    def strength(self):
        """Return the strength of the current bridge."""
        return sum([sum([port for port in piece]) for piece in self.bridge])

    def fitting_pieces(self):
        """Return a list of pieces that can be used to extend the current bridge."""
        return [piece for piece in self.available if self.port in piece]

    def add_piece(self, piece):
        """Return a new bridge with the piece added to it and removed from the available list."""
        new_bridge = self.bridge + [piece]
        # The new port is the unmatched port in the added piece
        new_port = piece[0] if piece[1] == self.port else piece[1]
        new_available = self.available[:]
        new_available.remove(piece)
        return Bridge(new_available, new_bridge, new_port)


def find_strongest(pieces):
    """Find strongest bridge constructable with a given list of pieces."""
    max_strength = 0
    queue = [Bridge(pieces)]
    while queue:
        bridge = queue.pop(0)
        fitting = bridge.fitting_pieces()
        if not fitting:
            strength = bridge.strength()
            if strength > max_strength:
                max_strength = strength
            continue

        for piece in fitting:
            queue.append(bridge.add_piece(piece))

    return max_strength


def find_strongest_longest(pieces):
    """Find strongest bridge from the longest bridges constructable with a list of pieces."""
    max_strength = max_length = 0
    queue = [Bridge(pieces)]
    while queue:
        bridge = queue.pop(0)
        fitting = bridge.fitting_pieces()
        if not fitting:
            length = len(bridge.bridge)
            if length > max_length:
                max_length = length
                max_strength = bridge.strength()
            elif length == max_length:
                strength = bridge.strength()
                if strength > max_strength:
                    max_strength = strength
                    max_length = length
            continue

        for piece in fitting:
            queue.append(bridge.add_piece(piece))

    return max_strength


def main():
    with open("input") as f:
        pieces = [[int(x), int(y)] for x, y in [p.split('/') for p in f.read().splitlines()]]

    #  print("Part 1:", find_strongest(pieces))
    print("Part 2:", find_strongest_longest(pieces))


if __name__ == "__main__":
    main()
