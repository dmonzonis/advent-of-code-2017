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

    part = input("Which part?[1]/2: ")
    if part == "2":
        step = len(inp) // 2
    else:
        step = 1

    print("Result:", sum_matching(inp, step))


if __name__ == "__main__":
    main()
