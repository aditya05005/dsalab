# Longest Common Subsequence (LCS) - Dynamic Programming.
# State: dp[i][j] = LCS length of X[..i] and Y[..j].
# Recurrence:
#   if X[i-1] == Y[j-1]: dp[i][j] = dp[i-1][j-1] + 1
#   else:                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# Complexity: O(m * n) time and space; backtrack to recover one LCS.


def lcs(x, y):
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack from dp[m][n] to build the subsequence.
    seq = []
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            seq.append(x[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return dp[m][n], "".join(reversed(seq)), dp


if __name__ == "__main__":
    # Hardcoded input
    x = "AGGTAB"
    y = "GXTXAYB"

    print(f"String X = {x}  (length {len(x)})")
    print(f"String Y = {y}  (length {len(y)})\n")

    length, seq, dp = lcs(x, y)

    print("DP table (rows = prefixes of X, cols = prefixes of Y):")
    print("       " + "".join(f"{c:>4}" for c in " " + y))
    for i in range(len(x) + 1):
        print(f"  {' ' if i == 0 else x[i - 1]:<4}" +
              "".join(f"{v:>4}" for v in dp[i]))

    print(f"\nLCS length = {length}")
    print(f"LCS        = {seq}")

    print("\nAnalysis: T(m, n) = O(m * n); each cell depends only on the cell")
    print("above, left, and diagonal (optimal substructure, overlapping subproblems).")
