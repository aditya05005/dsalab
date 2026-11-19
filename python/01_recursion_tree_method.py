# Recursion Tree Method: implementation and analysis of a recurrence.
# Recurrence: T(n) = 2*T(n/2) + n  (Merge Sort style)
# Recursion tree: level i has 2^i nodes, each costing (n / 2^i) -> cost per level = n.
# Tree depth = log2(n) -> total = n * log2(n) = O(n log n).
# This program builds the tree level by level, sums the costs, and verifies
# the closed form against a plain recursive T(n).


def recursion_tree_analysis(n):
    """Walk the recursion tree of T(n) = 2T(n/2) + n and sum level costs."""
    levels = []
    level = 0
    nodes = 1          # nodes at current level
    subproblem = n     # size of each subproblem at current level
    while subproblem > 1:
        level_cost = nodes * subproblem
        levels.append((level, nodes, subproblem, level_cost))
        nodes *= 2
        subproblem //= 2
        level += 1
    levels.append((level, nodes, subproblem, nodes * subproblem))  # leaf level
    total = sum(cost for _, _, _, cost in levels)
    return levels, total


def t_recursive(n):
    """Plain recursive T(n) = 2T(n/2) + n."""
    if n <= 1:
        return 1
    return 2 * t_recursive(n // 2) + n


if __name__ == "__main__":
    # Hardcoded input
    n = 16

    levels, total = recursion_tree_analysis(n)
    print(f"Recursion tree for T(n) = 2T(n/2) + n with n = {n}")
    print(f"{'Level':>5} | {'Nodes':>6} | {'Subproblem size':>15} | {'Level cost':>10}")
    print("-" * 50)
    for level, nodes, size, cost in levels:
        print(f"{level:>5} | {nodes:>6} | {size:>15} | {cost:>10}")
    print("-" * 50)
    print(f"Total cost from tree       : {total}")
    print(f"Closed form  n*log2(n)+n   : {n * (n.bit_length() - 1) + n}")
    print(f"Verified by recursion T(n) : {t_recursive(n)}")
    height = len(levels) - 1
    print(f"\nAnalysis: {height} internal levels, cost n per level")
    print("=> T(n) = O(n log n) [Master Method Case 2: a=2, b=2, f(n)=n]")
