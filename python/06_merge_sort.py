# Merge Sort (divide & conquer).
# Recurrence: T(n) = 2T(n/2) + n  ->  O(n log n)  (Master Method Case 2).
# Stable, not in-place; guaranteed O(n log n) in all cases.


def merge_sort(arr):
    """Return a new sorted list."""
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # <= keeps the sort stable
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out


if __name__ == "__main__":
    # Hardcoded input
    arr = [38, 27, 43, 3, 9, 82, 10, 27]

    print(f"Input : {arr}")
    result = merge_sort(arr)
    print(f"Output: {result}")

    print("\nTrace of divide steps:")
    def show(a, depth):
        if len(a) > 1:
            mid = len(a) // 2
            show(a[:mid], depth + 1)
            show(a[mid:], depth + 1)
        print("  " * depth + str(a))
    show(arr, 0)

    print("\nAnalysis: T(n) = 2T(n/2) + Theta(n)  =>  Theta(n log n),")
    print("Stable: equal elements keep original order (uses <= in merge).")
