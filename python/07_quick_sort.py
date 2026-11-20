# Quick Sort (divide & conquer with in-place partitioning).
# Best/Average recurrence: T(n) = 2T(n/2) + n  ->  O(n log n).
# Worst case (already sorted, first element pivot): T(n) = T(n-1) + n -> O(n^2).
# Uses Lomuto partition with last element as pivot; randomized pivot option below.


import random


def lomuto_partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1


def quick_sort(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        p = lomuto_partition(arr, lo, hi)
        quick_sort(arr, lo, p - 1)
        quick_sort(arr, p + 1, hi)
    return arr


def quick_sort_randomized(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        r = random.randint(lo, hi)
        arr[r], arr[hi] = arr[hi], arr[r]  # random pivot avoids worst case on sorted input
        p = lomuto_partition(arr, lo, hi)
        quick_sort_randomized(arr, lo, p - 1)
        quick_sort_randomized(arr, p + 1, hi)
    return arr


if __name__ == "__main__":
    # Hardcoded input
    arr = [10, 80, 30, 90, 40, 50, 70]

    print(f"Input : {arr}")
    result = quick_sort(arr[:])
    print(f"Output: {result}")

    arr2 = [5, 3, 8, 1, 9, 2, 7]
    print(f"Input : {arr2}")
    print(f"Output: {quick_sort(arr2[:])}")

    print("\nPartition trace example on last input:")
    demo = arr2[:]
    p = lomuto_partition(demo, 0, len(demo) - 1)
    print(f"after one Lomuto partition (pivot at index {p}): {demo}")
    print(f"Output: {quick_sort_randomized(demo)}")

    print("\nAnalysis: average T(n) = 2T(n/2) + Theta(n) => Theta(n log n);")
    print("worst case T(n) = T(n-1) + n => Theta(n^2); in-place, not stable.")
