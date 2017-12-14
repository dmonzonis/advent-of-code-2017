import sys
sys.path.append('../day10')

from day10 import knot_hash


def occupation_grid(inp, rows=128):
    """Return a list of strings containing 0 or 1 which represents the occupation grid."""
    grid = []
    for row in range(rows):
        string = inp + '-' + str(row)
        grid.append(''.join([bin(int(c, 16))[2:].zfill(4) for c in knot_hash(string)]))
    return grid


def occupied(grid):
    """Return the number of occupied slots in a binary grid."""
    count = 0
    for row in grid:
        count += row.count('1')
    return count


def main():
    grid = occupation_grid('ffayrhll')
    print("Part 1:", occupied(grid))


if __name__ == "__main__":
    main()
