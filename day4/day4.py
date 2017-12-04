def has_duplicates(s):
    seen = set()
    for e in s:
        if e in seen:
            return True
        seen.add(e)
    return False


def main():
    passphrases = []
    with open("input") as f:
        for line in f:
            passphrases.append(line.split())

    valids = [has_duplicates(p) for p in passphrases].count(False)
    print("Part 1:", valids)


if __name__ == "__main__":
    main()
