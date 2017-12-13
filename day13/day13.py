def parse_input(inp):
    """Parse input and return a dictionary containing range for each depth."""
    return {int(d): int(r) for d, r in [line.split(': ') for line in inp.splitlines()]}


def packet_severity(firewall):
    """Send a packet through a firewall and returns the total severity of the trip."""
    severity = 0
    max_depth = max(firewall.keys())
    for depth in range(max_depth + 1):
        if depth in firewall and depth % (2 * (firewall[depth] - 1)) == 0:
            # Packet caught
            severity += depth * firewall[depth]
    return severity


def packet_caught(firewall, delay=0):
    """Return whether the packet gets caught if sent through the firewall with a delay."""
    max_depth = max(firewall.keys())
    for depth in range(max_depth + 1):
        if depth in firewall and (depth + delay) % (2 * (firewall[depth] - 1)) == 0:
            return True
    return False


def packet_stealth_delay(firewall):
    """Compute the delay needed for a packet to travel without getting caught."""
    delay = 0
    while True:
        if not packet_caught(firewall, delay):
            return delay
        delay += 1


def main():
    with open("input") as f:
        inp = f.read().strip()

    firewall = parse_input(inp)

    print("Part 1:", packet_severity(firewall))
    print("Part 2:", packet_stealth_delay(firewall))


if __name__ == "__main__":
    main()
