def redistribution_cycles(seq):
    """Redistributes the largest number in a sequence until we get a repeated configuration of numbers"""
    seen = set()
    seen.add(get_configuration_id(seq))
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
            return cycles
        seen.add(new_config)


def get_configuration_id(seq):
    """Computes a unique identifier for the configuration of the list seq"""
    return hash(tuple(seq))


def main():
    with open("input") as f:
        seq = [int(x) for x in f.read().split()]

    print("Part 1:", redistribution_cycles(seq))


if __name__ == "__main__":
    main()
