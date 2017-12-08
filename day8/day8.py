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
    the state of all variables after the entire process, and the max value ever held
    """
    # Initialize variables to 0. Don't use defaultdict or get since we want info on the untouched
    # variables too, if any
    state = {}
    for variable, _, _ in instructions:
        state[variable] = 0
    max_value = 0

    # Run instructions one by one
    for variable, value, condition in instructions:
        # We need a condition using the state dictionary
        temp = condition.split()
        temp[0] = "state['%s']" % temp[0]
        condition = ' '.join(temp)
        if eval(condition):
            state[variable] += value
            if state[variable] > max_value:
                max_value = state[variable]

    return state, max_value


def main():
    instructions = []
    with open("input") as f:
        for line in f:
            instructions.append(parse_instruction(line))

    state, max_value = run_instructions(instructions)
    print("Part 1:", max(state.values()))
    print("Part 2:", max_value)


if __name__ == "__main__":
    main()
