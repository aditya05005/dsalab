# Binary Search on a sorted array.
# Invariant: if x exists, it lies within arr[lo..hi].
# Recurrence: T(n) = T(n/2) + 1 -> O(log n)  (Master Method Case 2, a=1, b=2)


def binary_search(arr, target):
    """Return index of target in sorted arr, or -1 if absent."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_recursive(arr, target, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, hi)
    return binary_search_recursive(arr, target, lo, mid - 1)


if __name__ == "__main__":
    # Hardcoded input
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    targets = [23, 2, 91, 7]

    print(f"Sorted array : {arr}")
    for t in targets:
        idx = binary_search(arr, t)
        ridx = binary_search_recursive(arr, t)
        assert idx == ridx
        print(f"search {t:>3}: index = {idx}")

    print("\nAnalysis: each comparison halves the search space.")
    print("Comparisons <= floor(log2 n) + 1  ;  Time O(log n), Space O(1) iterative.")
