def escape_maze(maze, part=1):
    """Escape the maze and return the total steps it took."""
    index = 0
    count = 0
    maze = maze[:]  # Make a copy so it doesn't modify the original
    while index < len(maze) and index >= 0:
        step = maze[index]
        if part == 2 and step >= 3:
            maze[index] -= 1
        else:
            maze[index] += 1
        index += step
        count += 1
    return count


def main():
    with open("input") as f:
        maze = [int(n) for n in f]

    print("Part 1:", escape_maze(maze))
    print("Part 2:", escape_maze(maze, part=2))


if __name__ == "__main__":
    main()
