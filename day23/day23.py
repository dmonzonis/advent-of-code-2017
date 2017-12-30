from collections import defaultdict


def parse_value(arg, register):
    """Return the value in the register if the input is a letter, or the value if it's an int."""
    try:
        return int(arg)
    except ValueError:
        return register[arg]


def count_mults(instructions):
    """Execute instructions and count the number of times a mult instruction is executed."""
    register = defaultdict(int)
    index = count = 0
    while 0 <= index < len(instructions):
        i = instructions[index]
        fun = i[0]
        if fun == 'set':
            register[i[1]] = parse_value(i[2], register)
        elif fun == 'sub':
            register[i[1]] -= parse_value(i[2], register)
        elif fun == 'mul':
            count += 1
            register[i[1]] *= parse_value(i[2], register)
        elif fun == 'jnz':
            if parse_value(i[1], register) != 0:
                index += parse_value(i[2], register)
                continue
        index += 1

    return count


def main():
    with open("input") as f:
        instructions = [line.split() for line in f.readlines()]

    print("Part 1:", count_mults(instructions))


if __name__ == "__main__":
    main()
