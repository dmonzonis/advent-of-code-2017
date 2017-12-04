def has_duplicates(s):
    seen = set()
    for e in s:
        if e in seen:
            return True
        seen.add(e)
    return False


def has_anagram(s):
    seen = set()
    for e in s:
        base = ''.join(sorted(e))
        if base in seen:
            return True
        seen.add(base)
    return False


def main():
    passphrases = []
    with open("input") as f:
        for line in f:
            passphrases.append(line.split())

    valids1 = [has_duplicates(p) for p in passphrases].count(False)
    valids2 = [has_anagram(p) for p in passphrases].count(False)
    print("Part 1:", valids1)
    print("Part 2:", valids2)


if __name__ == "__main__":
    main()
