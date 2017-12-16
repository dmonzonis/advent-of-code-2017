def spin(seq, size):
    seq = seq[-size:] + seq[:len(seq) - size]
    return seq


def exchange(seq, pos_a, pos_b):
    seq[pos_a], seq[pos_b] = seq[pos_b], seq[pos_a]
    return seq


def partner(seq, prog_a, prog_b):
    pos_a, pos_b = seq.index(prog_a), seq.index(prog_b)
    return exchange(seq, pos_a, pos_b)


def dance(seq, moves):
    """Parse and perform all the moves in the move list."""
    # Parse each move and its arguments, and execute it
    for move in moves:
        if move[0] == 's':
            # Spin
            size = int(move[1:])
            seq = spin(seq, size)
        elif move[0] == 'x':
            # Exchange
            pos_a, pos_b = [int(pos) for pos in move[1:].split('/')]
            seq = exchange(seq, pos_a, pos_b)
        elif move[0] == 'p':
            # Partner
            prog_a, prog_b = [prog for prog in move[1:].split('/')]
            seq = partner(seq, prog_a, prog_b)
    return seq


def main():
    with open("input") as f:
        moves = f.read().strip().split(',')

    seq = [chr(i) for i in range(ord('a'), ord('p') + 1)]

    after_dance = ''.join(dance(seq, moves))
    print("Part 1:", after_dance)


if __name__ == "__main__":
    main()
