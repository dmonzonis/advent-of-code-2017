from math import sqrt, ceil, floor


def manhattan_distance(n):
    # Using the lower negative diagonal (which are just the squares of odd
    # numbers) we can get the ring number
    ring = floor(ceil(sqrt(n)) / 2)
    # Steps to reach nearest axis
    offset = (n - (2 * ring - 1)**2) % (2 * ring)
    # Going to the nearest axis and traveling back from rings gives us the distance
    return ring + abs(offset - ring)


def main():
    print(manhattan_distance(368078))


if __name__ == "__main__":
    main()
