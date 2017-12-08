from collections import Counter


def find_root_node(parent_tree):
    node = list(parent_tree.keys())[0]  # Get a starting node
    # Go backwards until we find the root
    while node in parent_tree:
        node = parent_tree[node]
    return node


def generate_trees(inp):
    """
    Generates a bottom-up parent tree for quickly finding the root of the graph, and a
    regular top-down tree with weights
    """
    parent_tree = {}  # Keeps track of node's parent if it has any
    tree = {}
    for line in inp.splitlines():
        node = line.split()[0]
        weight = line.split()[1].strip('()')
        tree[node] = {'weight': int(weight)}

        if '->' in line:
            children = [s.strip() for s in line.split('->')[1].split(',')]
            tree[node].update({'children': children})
            for child in children:
                parent_tree[child] = node

    return tree, parent_tree


def find_weight_unbalance(tree, node):
    """
    Given a node and the graph tree, recursively finds an unbalance in its sublevels and returns the
    unbalance and True if the unbalance was found (assumes there's only one node with an unbalanced
    weight), or the total weight of the node and all of its subnodes and False if no unbalance was
    found
    """
    if 'children' not in tree[node]:
        return tree[node]['weight'], False

    weights = []
    for child in tree[node]['children']:
        weight, found = find_weight_unbalance(tree, child)
        if found:
            return weight, found
        weights.append(weight)

    # Check if there's an unbalance
    count = Counter(weights).most_common()
    if len(count) > 1:
        # Unbalance found
        diff = count[0][0] - count[1][0]
        unbalanced = tree[node]['children'][weights.index(count[1][0])]
        return tree[unbalanced]['weight'] + diff, True  # Set found flag to True

    return sum(weights) + tree[node]['weight'], False


def main():
    with open("input") as f:
        inp = f.read()
    tree, parent_tree = generate_trees(inp)
    root = find_root_node(parent_tree)

    print("Part 1:", root)

    unbalance, _ = find_weight_unbalance(tree, root)
    print("Part 2:", unbalance)


if __name__ == "__main__":
    main()
