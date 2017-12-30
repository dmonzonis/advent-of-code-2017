import string
from collections import defaultdict


def get_last_word(s):
    """Get the last word of a sentence ignoring punctuation."""
    return s.split()[-1].translate(str.maketrans('', '', string.punctuation))


def get_instruction_triplet(inp, index):
    """Return the parametrized instruction triplet below the index.

    Given the full input (separated by lines) and an index pointing to
    a sentence of the form "If the current value is x:", returns the
    three instructions below in a list, where the first value is the value which will be
    written, the second value is the direction value (1 or -1) and the third value is a char
    representing the next state.
    """
    val = int(get_last_word(inp[index + 1]))
    direction = get_last_word(inp[index + 2])
    # Translate direction to 1D unit vector
    if direction == 'right':
        direction = 1
    else:
        direction = -1
    next_state = get_last_word(inp[index + 3])
    return [val, direction, next_state]


def get_states(inp):
    """Return a dictionary containing parametrized insstructions for each state.

    States are represented as uppercase letters.
    Each state contains a list of two parametrized instruction triplets as generated
    by the get_instruction_triplet function, the first being the one corresponding to the case
    where the current value is 0, and the second to the case where the current value is 1.
    """
    states = {}
    i = 4
    letter = 'A'
    while i < len(inp):
        if_0 = get_instruction_triplet(inp, i)
        if_1 = get_instruction_triplet(inp, i + 4)
        states[letter] = [if_0, if_1]
        letter = chr(ord(letter) + 1)
        i += 10

    return states


def turing_checksum(states, steps, first_state='A'):
    """Run the Turing machine the given amount of steps and return the count of 1s after."""
    tape = defaultdict(int)
    pos = 0
    state = first_state
    for _ in range(steps):
        # Get corresponding set of instructions depending on value in current position
        instruction = states[state][tape[pos]]
        tape[pos] = instruction[0]
        pos += instruction[1]
        state = instruction[2]

    return sum([x == 1 for x in tape.values()])


def main():
    with open("input") as f:
        inp = f.readlines()

    states = get_states(inp)
    first_state = get_last_word(inp[0])
    checksum_count = int(inp[1].split()[-2])

    print("Part 1:", turing_checksum(states, checksum_count, first_state))


if __name__ == "__main__":
    main()
