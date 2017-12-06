def redistribution_cycles(seq):
    """
    Redistributes the largest number in a sequence until we get a repeated configuration of numbers
    and returns the total cycles it took, and the cycle difference between the repeated states
    """
    seen = {get_configuration_id(seq): 0}  # Store the cycle at which we found the state
    cycles = 0
    while True:
        stash = max(seq)  # Number to redistribute
        index = seq.index(stash)  # Position of the item being redistributed in the list
        seq[index] = 0
        while stash != 0:
            index += 1
            # If we reached the end, start over from the beginning
            if index == len(seq):
                index = 0
            seq[index] += 1
            stash -= 1
        cycles += 1
        # If we've seen the resulting configuration, we're done
        new_config = get_configuration_id(seq)
        if new_config in seen:
            return cycles, cycles - seen[new_config]
        seen[new_config] = cycles


def get_configuration_id(seq):
    """Computes a unique identifier for the configuration of the list seq"""
    return hash(tuple(seq))


def main():
    with open("input") as f:
        seq = [int(x) for x in f.read().split()]

    cycles, cycle_diff = redistribution_cycles(seq)
    print("Part 1:", cycles)
    print("Part 2:", cycle_diff)


if __name__ == "__main__":
    main()
