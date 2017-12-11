def direction(dir):
    """Given a direction string of the form 'ne', 's', etc returns the axial direction"""
    directions = {'n': (0, -1), 'ne': (1, -1), 'se': (1, 0), 's': (0, 1), 'sw': (-1, 1), 'nw': (-1, 0)}
    assert dir in directions
    return directions[dir]


def neighbor(pos, dir):
    """Given a position and a direction string, returns the neighbor hex position in that direction"""
    return tuple(map(sum, zip(pos, direction(dir))))


def distance(pos1, pos2):
    """Returns the distance in the hex grid using axial coordinates from one position to the other"""
    return (abs(pos1[0] - pos2[0]) +
            abs(pos1[0] + pos1[1] - pos2[0] - pos2[1]) +
            abs(pos1[1] - pos2[1])) // 2


def follow_path(path):
    """
    Starting from the origin, (0, 0), follows the path given as a list of direction strings
    and returns the final position
    """
    pos = (0, 0)
    for dir in path:
        pos = neighbor(pos, dir)
    return pos


def furthest_distance_path(path):
    """
    Starting from the origin, (0, 0), follows the path given as a list of direction strings
    and returns the maximum distance it ever gets from the origin
    """
    pos = origin = (0, 0)
    max = 0
    for dir in path:
        pos = neighbor(pos, dir)
        dist = distance(origin, pos)
        if dist > max:
            max = dist
    return max


def main():
    with open("input") as f:
        path = [dir for dir in f.read().strip().split(',')]

    print("Part 1:", distance((0, 0), follow_path(path)))
    print("Part 2:", furthest_distance_path(path))


if __name__ == "__main__":
    main()
