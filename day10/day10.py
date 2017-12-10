from functools import reduce


def to_ascii(string):
    """Converts a string to a list of numbers representing the ASCII value of each character"""
    return [ord(c) for c in string]


def knot_round(seq, lengths, reset=False):
    """
    Given a sequence of numbers and a list of lengths, modifies the sequence after a single round of the
    knot hash algorithm, and saves variable status since it's a generator
    """
    limit = len(seq)
    left = skip = 0
    while True:
        if reset:
            left = skip = 0

        for length in lengths:
            right = (left + length) % limit
            if left >= right and length > 0:
                # Selection wraps around the list
                wrapping_point = limit - left
                selected = list(reversed(seq[left:] + seq[:right]))
                seq[left:] = selected[:wrapping_point]
                seq[:right] = selected[wrapping_point:]
            else:
                seq[left:right] = reversed(seq[left:right])

            left = (right + skip) % limit
            skip += 1

        yield


def knot_hash(string):
    """Returns the knot hash of a string"""
    ROUNDS = 64
    # Get the length list from the string, and add the constant suffix
    lengths = to_ascii(string)
    lengths.extend([17, 31, 73, 47, 23])
    seq = list(range(256))
    hash_generator = knot_round(seq, lengths)
    # Execute all the rounds of the algorithm with the same length list, updating seq each time
    for _ in range(ROUNDS):
        next(hash_generator)

    # XOR each chunk of 16 numbers and format as a hex string
    code = [reduce((lambda x, y: x ^ y), seq[i:i + 16]) for i in range(0, len(seq), 16)]
    result = ''.join([format(n, 'x').zfill(2) for n in code])
    return result


def main():
    # Part 1
    with open("input") as f:
        lengths = [int(n) for n in f.read().strip().split(',')]

    seq = list(range(256))
    seq_generator = knot_round(seq, lengths)
    next(seq_generator)
    print("Part 1:", seq[0] * seq[1])

    # Part 2
    with open("input") as f:
        string = f.read().strip()
    hashed = knot_hash(string)
    print("Part 2:", hashed)


if __name__ == "__main__":
    main()
