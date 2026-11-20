# 0/1 Knapsack - Dynamic Programming.
# State: dp[i][w] = best value using first i items with capacity w.
# Recurrence:
#   dp[i][w] = dp[i-1][w]                                (item i excluded)
#   dp[i][w] = max(dp[i-1][w], values[i] + dp[i-1][w-wt[i]])  (included, if it fits)
# Greedy is NOT optimal for 0/1; DP explores both choices.
# Complexity: O(n * W) time and space (O(W) with 1-D rolling array).


def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w],
                               values[i - 1] + dp[i - 1][w - weights[i - 1]])

    # Reconstruct which items were taken by walking back through the table.
    items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items.append(i - 1)
            w -= weights[i - 1]
    items.reverse()
    return dp[n][capacity], items, dp


if __name__ == "__main__":
    # Hardcoded input
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    n = len(values)
    print(f"Items: value={values}, weight={weights}, capacity={capacity}\n")

    best, items, dp = knapsack_01(values, weights, capacity)

    print(f"DP table (rows = items considered 0..{n}, cols = capacity 0..{capacity}):")
    header = "     " + "".join(f"{w:>5}" for w in range(capacity + 1))
    print(header)
    for i in range(n + 1):
        print(f"i={i:<3}" + "".join(f"{v:>5}" for v in dp[i]))

    print(f"\nOptimal value = {best}")
    print("Items taken:")
    total_w = 0
    for i in items:
        print(f"  item {i + 1}: value={values[i]}, weight={weights[i]}")
        total_w += weights[i]
    print(f"Total weight used = {total_w} / {capacity}")

    print("\nAnalysis: T(n) = O(n * W) pseudo-polynomial; each cell computed in O(1)")
    print("from two smaller subproblems (overlapping subproblems + optimal substructure).")
