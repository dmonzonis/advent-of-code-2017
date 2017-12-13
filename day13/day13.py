def parse_input(inp):
    """Parse input and return a dictionary containing range for each depth."""
    return {int(d): int(r) for d, r in [line.split(': ') for line in inp.splitlines()]}


def packet_travel(firewall):
    """Send a packet through a firewall and returns the total severity of the trip."""
    severity = 0
    max_depth = max(firewall.keys())
    for depth in range(max_depth + 1):
        if depth in firewall and depth % (2 * (firewall[depth] - 1)) == 0:
            # Packet caught
            severity += depth * firewall[depth]
    return severity


def main():
    with open("input") as f:
        inp = f.read().strip()

    firewall = parse_input(inp)

    print("Part 1:", packet_travel(firewall))
    #  print("Part 2:", packet_stealth_delay(firewall))


if __name__ == "__main__":
    main()
