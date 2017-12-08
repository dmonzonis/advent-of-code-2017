def parse_instruction(p):
    p = p.split()
    variable = p[0]
    sign = 1 if p[1] == 'inc' else -1
    value = int(p[2]) * sign
    condition = ' '.join(p[4:])
    return variable, value, condition


def run_instructions(instructions):
    """
    Executes all the instructions passed as an argument and returns a dictionary containing
    the state of all variables after the entire process
    """
    # Initialize variables to 0. Don't use defaultdict or get since we want info on the untouched
    # variables too, if any
    state = {}
    for variable, _, _ in instructions:
        state[variable] = 0

    # Run instructions one by one
    for variable, value, condition in instructions:
        # We need a condition using the state dictionary
        temp = condition.split()
        temp[0] = "state['%s']" % temp[0]
        condition = ' '.join(temp)
        if eval(condition):
            state[variable] += value

    return state


def main():
    instructions = []
    with open("input") as f:
        for line in f:
            instructions.append(parse_instruction(line))

    state = run_instructions(instructions)
    print("Part 1:", max(state.values()))


if __name__ == "__main__":
    main()
