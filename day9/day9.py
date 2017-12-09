def skip_garbage(stream, index):
    """
    Returns the index after the garbage closing tag, and the number of non-canceled garbage
    characters
    """
    garbage = 0
    # Index points to the first character after the garbage starting point
    while True:
        if stream[index] == '!':
            index += 2
        elif stream[index] == '>':
            return index + 1, garbage
        else:
            index += 1
            garbage += 1


def scan_stream(stream):
    """Returns the score and the total non-canceled garbage of the stream"""
    index = depth = score = total_garbage = 0
    while index < len(stream):
        if stream[index] == '{':
            index += 1
            depth += 1
        elif stream[index] == '<':
            index, garbage = skip_garbage(stream, index + 1)
            total_garbage += garbage
        elif stream[index] == '}':
            index += 1
            score += depth
            depth -= 1
        else:
            index += 1

    return score, total_garbage


def main():
    with open("input") as f:
        inp = f.read()

    score, garbage = scan_stream(inp)
    print("Part 1:", score)
    print("Part 2:", garbage)


if __name__ == "__main__":
    main()
