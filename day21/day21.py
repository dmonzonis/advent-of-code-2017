import numpy as np


class Rulebook:
    """Holds the rules to enhance blocks of art."""

    def __init__(self, rules):
        self.rules = rules
        self.cache = {}
        self._build_cache()

    def _build_cache(self):
        # Map every possible rotation and flipped rotation of the same input to the same result
        for rule, enhanced in self.rules:
            for rot in range(4):
                self.cache[matrix_to_pattern(rule)] = enhanced
                rule = np.rot90(rule)
            rule = np.flip(rule, axis=1)
            for rot in range(4):
                self.cache[matrix_to_pattern(rule)] = enhanced
                rule = np.rot90(rule)

    def enhance_pattern(self, pattern):
        """Search for a matching pattern in the rules and apply the corresponding enhancing rule."""
        return self.cache[matrix_to_pattern(pattern)]


def pattern_to_matrix(pattern):
    """Convert a pattern given as a string to a boolean numpy array."""
    pattern = pattern.split('/')
    for i in range(len(pattern)):
        pattern[i] = list(pattern[i])
    return np.array(pattern) == '#'


def matrix_to_pattern(matrix):
    """Convert a pattern given as a boolean numpy array to a string pattern."""
    res = ''
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Translate Trues to '#' and Falses to '.'
            if matrix[i, j]:
                res += '#'
            else:
                res += '.'
        res += '/'
    return res[:-1]  # We don't want the last slash


def parse_rules(inp):
    """Given a set of rules written as strings, return the corresponding rulebook."""
    rules = []
    for line in inp:
        pattern, result = line.split(' => ')
        rules.append(
            (pattern_to_matrix(pattern),
             pattern_to_matrix(result))
        )
    return Rulebook(rules)


def generate_art(pattern, rulebook, iterations):
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
                enhanced = rulebook.enhance_pattern(pattern[i:i + step, j:j + step])
                pattern_row = np.hstack((pattern_row, enhanced))
            art = np.vstack((art, pattern_row))

        pattern = art

    return art


def main():
    with open("input") as f:
        inp = f.read().splitlines()

    rulebook = parse_rules(inp)
    pattern = pattern_to_matrix('.#./..#/###')

    art = generate_art(pattern, rulebook, 5)
    print("Part 1:", np.sum(art))

    art = generate_art(art, rulebook, 13)
    print("Part 2:", np.sum(art))


if __name__ == "__main__":
    main()
