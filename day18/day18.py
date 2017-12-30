from collections import defaultdict


class Program:
    def __init__(self, id):
        self.queue = []
        self.register = defaultdict(int)
        self.register['p'] = id
        self.companion = None
        self.index = self.sent = 0
        self.done = False

    def add_companion(self, other):
        self.companion = other

    def send_value_to_companion(self, value):
        if self.companion is None:
            raise ValueError("Program doesn't have a companion")
        self.companion.queue.append(value)

    def execute_instructions(self, instructions):
        while 0 <= self.index < len(instructions):
            i = instructions[self.index]
            fun = i[0]
            if fun == 'set':
                self.register[i[1]] = parse_value(i[2], self.register)
            elif fun == 'snd':
                self.send_value_to_companion(parse_value(i[1], self.register))
                self.sent += 1
            elif fun == 'add':
                self.register[i[1]] += parse_value(i[2], self.register)
            elif fun == 'mul':
                self.register[i[1]] *= parse_value(i[2], self.register)
            elif fun == 'mod':
                self.register[i[1]] %= parse_value(i[2], self.register)
            elif fun == 'rcv':
                if not self.queue:
                    if not self.companion.queue or self.companion.done:
                        self.done = True
                    return
                else:
                    self.done = False
                    self.register[i[1]] = self.queue.pop(0)
            elif fun == 'jgz':
                if parse_value(i[1], self.register) > 0:
                    self.index += parse_value(i[2], self.register)
                    continue

            self.index += 1

        self.done = True


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
            if parse_value(i[1], register) > 0:
                n += parse_value(i[2], register)
                continue
        n += 1


def duet(instructions):
    """Simulate both programs sending values to each other and following instructions.

    Return the amount of times program 1 sent a value.
    """
    # Initialize programs
    program0 = Program(0)
    program1 = Program(1)
    program0.add_companion(program1)
    program1.add_companion(program0)

    while True:
        program0.execute_instructions(instructions)
        program1.execute_instructions(instructions)
        if program0.done and program1.done:
            return program1.sent

def main():
    with open("input") as f:
        instructions = [line.split() for line in f.readlines()]

    print("Part 1:", recover_frequency(instructions))
    print("Part 2:", duet(instructions))


if __name__ == "__main__":
    main()
