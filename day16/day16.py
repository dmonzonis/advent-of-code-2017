from functools import partial


def spin(seq, size):
    seq = seq[-size:] + seq[:len(seq) - size]
    return seq


def exchange(seq, pos_a, pos_b):
    seq = seq[:]
    seq[pos_a], seq[pos_b] = seq[pos_b], seq[pos_a]
    return seq


def partner(seq, prog_a, prog_b):
    seq = seq[:]
    pos_a, pos_b = seq.index(prog_a), seq.index(prog_b)
    return exchange(seq, pos_a, pos_b)


def parse_moves(moves):
    """Parse a list of moves and return a list of partials that perform each move."""
    res = []
    for move in moves:
        if move[0] == 's':
            # Spin
            size = int(move[1:])
            part = partial(spin, size=size)
        elif move[0] == 'x':
            # Exchange
            pos_a, pos_b = [int(pos) for pos in move[1:].split('/')]
            part = partial(exchange, pos_a=pos_a, pos_b=pos_b)
        elif move[0] == 'p':
            # Partner
            prog_a, prog_b = [prog for prog in move[1:].split('/')]
            part = partial(partner, prog_a=prog_a, prog_b=prog_b)

        res.append(part)
    return res


def dance(seq, partials):
    """Parse and perform all the moves in a partial list."""
    seq = seq[:]
    # Parse each move and its arguments, and execute it
    for move in partials:
        seq = move(seq)
    return seq


def repeat_dance(seq, partials, times=1000000000):
    """Repeat dance until we're done or we find a cycle, and return the final result."""
    seen = []
    for t in range(times):
        s = ''.join(seq)
        # If there's a cycle, we don't need to go on
        if s in seen:
            return(seen[times % t])
        seen.append(s)
        seq = dance(seq, partials)
    return seq


def main():
    with open("input") as f:
        moves = f.read().strip().split(',')

    seq = [chr(i) for i in range(ord('a'), ord('p') + 1)]

    partials = parse_moves(moves)
    after_dance = dance(seq, partials)
    print("Part 1:", ''.join(after_dance))

    print("Part 2:", ''.join(repeat_dance(seq, partials)))


if __name__ == "__main__":
    main()
