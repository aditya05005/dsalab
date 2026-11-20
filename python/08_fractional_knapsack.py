# Fractional (Continuous) Knapsack - Greedy Algorithm.
# Greedy choice: take items in decreasing order of value/weight ratio;
# take whole items while they fit, then take a FRACTION of the next item.
# Greedy is optimal here (exchange argument), unlike 0/1 knapsack.
# Complexity: O(n log n) for sorting + O(n) scan.


def fractional_knapsack(values, weights, capacity):
    """Return (max_value, selections) where selections[i] is the fraction
    of item i placed in the knapsack (0..1)."""
    n = len(values)
    order = sorted(range(n), key=lambda i: values[i] / weights[i], reverse=True)
    selections = [0.0] * n
    total = 0.0
    remaining = capacity
    for i in order:
        if weights[i] <= remaining:
            selections[i] = 1.0
            total += values[i]
            remaining -= weights[i]
        else:
            selections[i] = remaining / weights[i]
            total += values[i] * selections[i]
            remaining = 0.0
            break
    return total, selections, order


if __name__ == "__main__":
    # Hardcoded input
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    print(f"Items (value, weight): {list(zip(values, weights))}")
    print(f"Knapsack capacity    : {capacity}\n")

    for i in range(len(values)):
        print(f"  item {i}: value={values[i]:>3}, weight={weights[i]:>2}, "
              f"ratio={values[i] / weights[i]:.2f}")

    total, selections, order = fractional_knapsack(values, weights, capacity)

    print(f"\nGreedy order by ratio: {order}")
    print("Selections:")
    for i, frac in enumerate(selections):
        if frac > 0:
            print(f"  take {frac:.4f} of item {i} "
                  f"(value {values[i] * frac:.2f}, weight {weights[i] * frac:.2f})")

    print(f"\nTotal value = {total:.2f}")
    print("Analysis: T(n) = O(n log n) (sort dominant); greedy is optimal for")
    print("fractional knapsack but NOT for 0/1 knapsack (use DP instead).")
