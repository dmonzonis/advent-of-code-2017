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


def explore(grid, row, col, visited):
    """Explores the region starting at (row, col), adding elements to visited."""
    # Check if the slot is not occupied or has been visited
    if (row, col) in visited or grid[row][col] == '0':
        return

    # Visit the slot
    visited.add((row, col))

    # Recursively visit adjacent occupied slots
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for direction in directions:
        # Move a slot in that direction
        new_row, new_col = [sum(x) for x in zip((row, col), direction)]
        # Check if we're out of bounds
        if new_row >= len(grid) or new_row < 0 or new_col >= len(grid) or new_col < 0:
            continue

        explore(grid, new_row, new_col, visited)


def occupied_regions(grid):
    """Return the number of occupied regions in the binary grid."""
    visited = set()
    regions = 0

    for row in range(len(grid)):
        for col in range(len(grid)):
            # If we found an unexplored region, explore it
            if grid[row][col] == '1' and (row, col) not in visited:
                explore(grid, row, col, visited)
                regions += 1

    return regions


def main():
    grid = occupation_grid('ffayrhll')
    print("Part 1:", occupied(grid))
    print("Part 2:", occupied_regions(grid))


if __name__ == "__main__":
    main()
