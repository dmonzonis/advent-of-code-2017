from collections import defaultdict


def parse_value(arg, register):
    """Return the value in the register if the input is a letter, or the value if it's an int."""
    try:
        return int(arg)
    except ValueError:
        return register[arg]


def recover_frequency(instructions):
    """Execute instructions and return the recovered frequency."""
    register = defaultdict(int)
    last = n = 0
    while n >= 0 and n < len(instructions):
        i = instructions[n]
        fun = i[0]
        if fun == 'set':
            register[i[1]] = parse_value(i[2], register)
        elif fun == 'snd':
            last = parse_value(i[1], register)
        elif fun == 'add':
            register[i[1]] += parse_value(i[2], register)
        elif fun == 'mul':
            register[i[1]] *= parse_value(i[2], register)
        elif fun == 'mod':
            register[i[1]] %= parse_value(i[2], register)
        elif fun == 'rcv':
            if parse_value(i[1], register) != 0:
                return last
        elif fun == 'jgz':
            if parse_value(i[1], register) != 0:
                n += parse_value(i[2], register)
                continue
        n += 1


def main():
    with open("input") as f:
        instructions = [line.split() for line in f.readlines()]

    print("Part 1:", recover_frequency(instructions))


if __name__ == "__main__":
    main()
