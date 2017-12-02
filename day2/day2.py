def checksum(matrix):
    return sum([max(row) - min(row) for row in matrix])


def find_divisible_pair(p):
    assert len(p) > 1

    checkpoint = 1
    for i in p:
        for j in p[checkpoint:]:
            # Return a tuple (dividend, divisor)
            if i % j == 0:
                return i, j
            if j % i == 0:
                return j, i
        checkpoint += 1


def main():
    matrix = []
    with open("input") as f:
        for line in f:
            row = [int(x) for x in line.split('\t')]
            matrix.append(row)

    print("Part 1:", checksum(matrix))

    print("Part 2:", sum([fst // snd for fst, snd in [find_divisible_pair(row) for row in matrix]]))


if __name__ == "__main__":
    main()
