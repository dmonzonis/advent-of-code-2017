def sum_matching(s):
    assert len(s) > 1

    current = s[0]
    result = 0
    for next in s[1:]:
        if current == next:
            result += int(next)

    if s[0] == s[-1]:
        result += int(s[0])

    return result


def main():
    with open("input") as f:
        inp = f.read().strip()

    print("Result:", sum_matching(inp))


if __name__ == "__main__":
    main()
