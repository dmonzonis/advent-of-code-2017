def knot_hash(lengths, limit=256):
    """
    Given a list of lengths, returns the knot hash of a list of a fixed amount of elements, going from 0
    to limit - 1
    """
    seq = list(range(limit))
    left = skip = 0
    for length in lengths:
        right = (left + length) % limit
        if length <= 0 or length > limit:
            # Invalid length, don't update sequence
            pass
        elif left >= right:
            # Selection wraps around the list
            wrapping_point = limit - left
            selected = list(reversed(seq[left:] + seq[:right]))
            seq[left:] = selected[:wrapping_point]
            seq[:right] = selected[wrapping_point:]
        else:
            seq[left:right] = reversed(seq[left:right])

        left = (right + skip) % limit
        skip += 1

    return seq


def main():
    with open("input") as f:
        lengths = [int(n) for n in f.read().strip().split(',')]

    hashed = knot_hash(lengths)
    print("Part 1:", hashed[0] * hashed[1])


if __name__ == "__main__":
    main()
