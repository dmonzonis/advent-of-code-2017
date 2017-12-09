def skip_garbage(stream, index):
    # Index points to the first character after the garbage starting point
    while True:
        if stream[index] == '!':
            index += 2
        elif stream[index] == '>':
            return index + 1
        else:
            index += 1


def scan_stream(stream):
    index, depth, result = 0, 0, 0
    while index < len(stream):
        if stream[index] == '{':
            index += 1
            depth += 1
        elif stream[index] == '<':
            index = skip_garbage(stream, index)
        elif stream[index] == '}':
            index += 1
            result += depth
            depth -= 1
        else:
            index += 1

    return result


def main():
    with open("input") as f:
        inp = f.read()

    print("Part 1:", scan_stream(inp))


if __name__ == "__main__":
    main()
