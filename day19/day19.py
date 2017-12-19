def step(pos, direction):
    """Take a step in a given direction and return the new position."""
    return [sum(x) for x in zip(pos, direction)]


def turn_left(direction):
    """Return a new direction resulting from turning 90 degrees left."""
    return (direction[1], -direction[0])


def turn_right(direction):
    """Return a new direction resulting from turning 90 degrees right."""
    return (-direction[1], direction[0])


def get_tile(roadmap, pos):
    """With a position in the form (x, y), return the tile in the roadmap corresponding to it."""
    x, y = pos
    return roadmap[y][x]


def follow_roadmap(roadmap):
    """Follow the roadmap until the end and return the list of characters encountered."""
    direction = (0, 1)  # Start going down
    valid_tiles = ['-', '|', '+']  # Valid road tiles
    collected = []
    pos = (roadmap[0].index('|'), 0)  # Initial position in the form (x, y)

    while True:
        new_pos = step(pos, direction)
        tile = get_tile(roadmap, new_pos)
        if tile == ' ':
            # Look for a new direction left or right
            if get_tile(roadmap, step(pos, turn_left(direction))) != ' ':
                direction = turn_left(direction)
                continue
            elif get_tile(roadmap, step(pos, turn_right(direction))) != ' ':
                direction = turn_right(direction)
                continue
            else:
                # We got to the end of the road
                return collected

        elif tile not in valid_tiles:
            collected.append(tile)

        pos = new_pos


def main():
    with open("input") as f:
        roadmap = f.read().split('\n')

    collected = follow_roadmap(roadmap)
    print("Part 1:", ''.join(collected))


if __name__ == "__main__":
    main()
