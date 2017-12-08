def find_root_node(parent_tree):
    node = list(parent_tree.keys())[0]  # Get a starting node
    # Go backwards until we find the root
    while node in parent_tree:
        node = parent_tree[node]
    return node


def generate_parent_tree(inp):
    parent_tree = {}  # Keeps track of node's parent if it has any
    for line in inp.splitlines():
        process = line.split()[0]
        #  weight = line.split()[1].strip('()')

        if '->' in line:
            children = [s.strip() for s in line.split('->')[1].split(',')]
            for child in children:
                parent_tree[child] = process

    return parent_tree


def main():
    with open("input") as f:
        inp = f.read()
    tree = generate_parent_tree(inp)
    root = find_root_node(tree)

    print("Part 1:", root)


if __name__ == "__main__":
    main()
