# B-Tree of minimum degree t.
# Rules:
#   - every node has at most 2t-1 keys
#   - every non-root internal node has at least t-1 keys
#   - root has at least 1 key (if not leaf)
#   - all leaves at same depth
# Insert splits full children on the way down (proactive splitting).


class BTreeNode:
    def __init__(self, leaf):
        self.leaf = leaf
        self.keys = []
        self.children = []


class BTree:
    def __init__(self, t):
        self.t = t
        self.root = BTreeNode(True)

    def search(self, key, node=None):
        node = self.root if node is None else node
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and node.keys[i] == key:
            return node
        if node.leaf:
            return None
        return self.search(key, node.children[i])

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _split_child(self, parent, i):
        t = self.t
        child = parent.children[i]
        right = BTreeNode(child.leaf)
        mid = child.keys[t - 1]
        right.keys = child.keys[t:]
        child.keys = child.keys[: t - 1]
        if not child.leaf:
            right.children = child.children[t:]
            child.children = child.children[:t]
        parent.keys.insert(i, mid)
        parent.children.insert(i + 1, right)

    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(0)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.t - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def print_tree(self, node=None, level=0):
        node = self.root if node is None else node
        label = "  " * level + f"[L{level}] " + " ".join(map(str, node.keys))
        print(label)
        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level + 1)


if __name__ == "__main__":
    # Hardcoded input
    keys = [10, 20, 5, 6, 12, 30, 7, 17, 3, 25, 1, 40, 8]

    t = 3
    tree = BTree(t)
    for k in keys:
        tree.insert(k)

    print(f"B-Tree of minimum degree t={t}, inserted order: {keys}\n")
    print("Tree structure (root first, leaves last):")
    tree.print_tree()

    find = 6
    print(f"\nSearch {find}: {'FOUND' if tree.search(find) else 'NOT FOUND'}")
    find = 100
    print(f"Search {find}: {'FOUND' if tree.search(find) else 'NOT FOUND'}")

    ks = sorted(keys)
    root = tree.root
    print(f"\nAnalysis: root holds {len(root.keys)} keys {root.keys}; "
          f"min degree {t} allows 1..{2 * t - 1} keys per node.")
    print(f"In-order keys      : {ks}")
    print(f"Height is O(log_t n) -> search/insert in O(t * log_t n) = O(log n) with fixed t.")
