import numpy as np


def _check_match_rotation(a, b):
    for rot in range(4):
        if (a == b).all():
            return True
        a = np.rot90(a)
    return False


def check_match(a, b):
    """Check if pattern a matches pattern b by rotating and flipping."""
    if a.shape != b.shape:
        return False
    if _check_match_rotation(a, b):
        return True
    a = np.flip(a, axis=1)
    return _check_match_rotation(a, b)


def enhance_pattern(pattern, rules):
    """Search for a matching pattern in the rules and apply the corresponding enhancing rule."""
    for rule, enhanced in rules:
        if check_match(pattern, rule):
            return enhanced


def pattern_to_matrix(pattern):
    """Convert a pattern given as a string to a boolean numpy array."""
    pattern = pattern.split('/')
    for i in range(len(pattern)):
        pattern[i] = list(pattern[i])
    return np.array(pattern) == '#'


def parse_rules(inp):
    """Given a set of rules written as strings, return a list of tuples with matrix rules."""
    rules = []
    for line in inp:
        pattern, result = line.split(' => ')
        rules.append(
            (pattern_to_matrix(pattern),
             pattern_to_matrix(result))
        )
    return rules


def generate_art(pattern, rules, iterations):
    """Apply the enhancement rules for n iterations, using an initial pattern."""
    for _ in range(iterations):
        dim = pattern.shape[0]
        if dim % 2 == 0:
            part = dim // 2
            step = 2
        elif dim % 3 == 0:
            part = dim // 3
            step = 3

        art = np.array([], dtype=bool).reshape(0, dim + part)
        for i in range(0, dim, step):
            pattern_row = np.array([], dtype=bool).reshape(step + 1, 0)
            for j in range(0, dim, step):
                enhanced = enhance_pattern(pattern[i:i + step, j:j + step], rules)
                pattern_row = np.hstack((pattern_row, enhanced))
            art = np.vstack((art, pattern_row))

        pattern = art

    return art


def main():
    with open("input") as f:
        inp = f.read().splitlines()

    rules = parse_rules(inp)
    pattern = pattern_to_matrix('.#./..#/###')

    art = generate_art(pattern, rules, 5)
    print("Part 1:", np.sum(art))

    art = generate_art(art, rules, 13)
    print("Part 2:", np.sum(art))


if __name__ == "__main__":
    main()
