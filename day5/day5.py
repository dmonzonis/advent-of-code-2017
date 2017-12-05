def escape_maze(maze):
    """Escape the maze and return the total steps it took."""
    index = 0
    count = 0
    while index < len(maze) and index >= 0:
        step = maze[index]
        maze[index] += 1
        index += step
        count += 1
    return count


def main():
    with open("input") as f:
        maze = [int(n) for n in f]

    print("Part 1:", escape_maze(maze))


if __name__ == "__main__":
    main()
