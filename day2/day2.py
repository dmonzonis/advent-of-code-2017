def checksum(matrix):
    return sum([max(row) - min(row) for row in matrix])


def main():
    matrix = []
    with open("input") as f:
        for line in f:
            row = [int(x) for x in line.split('\t')]
            matrix.append(row)

    print("Result:", checksum(matrix))


if __name__ == "__main__":
    main()
