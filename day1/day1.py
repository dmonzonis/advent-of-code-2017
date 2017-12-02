def sum_matching(s, step):
    assert len(s) > 1

    current = s[0]
    result = 0
    for i in range(len(s)):
        current = s[i]
        if current == s[(i + step) % len(s)]:
            result += int(current)

    return result


def main():
    with open("input") as f:
        inp = f.read().strip()

    print("Result:", sum_matching(inp, len(inp) // 2))


if __name__ == "__main__":
    main()
