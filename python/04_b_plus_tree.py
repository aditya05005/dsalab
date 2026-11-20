# B+ Tree of order m (max children per node = m; leaves hold all data, linked).
# Internal nodes store routing keys only; all real keys live in the leaves,
# and leaves are chained left-to-right for fast range scan.


class BPlusNode:
    def __init__(self, leaf):
        self.leaf = leaf
        self.keys = []
        self.children = []
        self.next = None  # sibling link for leaves


class BPlusTree:
    def __init__(self, order):
        self.order = order
        self.root = BPlusNode(True)

    def _max_keys(self):
        return self.order - 1

    def _min_keys(self):
        return self.order // 2 - 1

    def search(self, key):
        node = self.root
        while not node.leaf:
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            node = node.children[i]
        return node if key in node.keys else None

    def insert(self, key):
        result = self._insert(self.root, key)
        if result is None:
            return
        median, right = result
        new_root = BPlusNode(False)
        new_root.keys = [median]
        new_root.children = [self.root, right]
        self.root = new_root

    def _insert(self, node, key):
        if node.leaf:
            pos = 0
            while pos < len(node.keys) and key > node.keys[pos]:
                pos += 1
            node.keys.insert(pos, key)
        else:
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            result = self._insert(node.children[i], key)
            if result is None:
                return None
            median, right = result
            node.keys.insert(i, median)
            node.children.insert(i + 1, right)
        if len(node.keys) <= self._max_keys():
            return None
        return self._split(node)

    def _split(self, node):
        if node.leaf:
            split = len(node.keys) // 2 + 1  # copy-up for leaves
            right = BPlusNode(True)
            right.keys = node.keys[split:]
            node.keys = node.keys[:split]
            right.next = node.next
            node.next = right
            return right.keys[0], right
        split = len(node.keys) // 2  # move-up for internal nodes
        median = node.keys[split]
        right = BPlusNode(False)
        right.keys = node.keys[split + 1:]
        right.children = node.children[split + 1:]
        node.keys = node.keys[:split]
        node.children = node.children[:split + 1]
        return median, right

    def leaves(self):
        """Collect all leaf nodes left-to-right."""
        node = self.root
        while not node.leaf:
            node = node.children[0]
        chain = []
        while node is not None:
            chain.append(node)
            node = node.next
        return chain

    def range_query(self, lo, hi):
        """Scan the leaf chain for keys in [lo, hi]."""
        out = []
        node = self.root
        while not node.leaf:
            i = 0
            while i < len(node.keys) and lo >= node.keys[i]:
                i += 1
            node = node.children[i]
        while node is not None:
            for k in node.keys:
                if lo <= k <= hi:
                    out.append(k)
                if k > hi:
                    return out
            node = node.next
        return out

    def print_tree(self, node=None, level=0):
        node = self.root if node is None else node
        kind = "LEAF" if node.leaf else "INT "
        print("  " * level + f"[{kind} L{level}] " + " ".join(map(str, node.keys)))
        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level + 1)


if __name__ == "__main__":
    # Hardcoded input
    keys = [10, 20, 5, 6, 12, 30, 7, 17, 3, 25, 1, 40, 8]

    order = 4
    tree = BPlusTree(order)
    for k in keys:
        tree.insert(k)

    print(f"B+ Tree of order {order}, inserted order: {keys}\n")
    print("Tree structure:")
    tree.print_tree()

    leaves = tree.leaves()
    print("\nLeaf chain (all data, linked):")
    print(" -> ".join("[" + ", ".join(map(str, leaf.keys)) + "]" for leaf in leaves))

    find = 12
    print(f"\nPoint search {find}: {'FOUND in leaf' if tree.search(find) else 'NOT FOUND'}")
    find = 99
    print(f"Point search {find}: {'FOUND in leaf' if tree.search(find) else 'NOT FOUND'}")

    lo, hi = 6, 25
    print(f"Range query [{lo}, {hi}] via leaf chain: {tree.range_query(lo, hi)}")

    print("\nAnalysis: all keys in leaves, internal nodes only route.")
    print("Point ops: O(log n). Range scan: O(log n + result size) by walking leaf links.")
