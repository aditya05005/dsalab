# Master Method: implementation and analysis of recurrences of the form
#   T(n) = a * T(n/b) + f(n),  a >= 1, b > 1.
# Cases:
#   1. f(n) = O(n^(log_b a - eps))        -> T(n) = Theta(n^(log_b a))
#   2. f(n) = Theta(n^(log_b a) * log^k n)-> T(n) = Theta(n^(log_b a) * log^(k+1) n)
#   3. f(n) = Omega(n^(log_b a + eps)) with regularity a*f(n/b) <= c*f(n)
#                                          -> T(n) = Theta(f(n))


def log_b(a, b):
    """log_b(a) computed with enough precision for comparison."""
    import math
    return math.log(a) / math.log(b)


def master_method(a, b, fn_degree, fn_log_power=0):
    """Classify T(n) = a T(n/b) + Theta(n^fn_degree * log^fn_log_power n).

    Returns (case_number, asymptotic_solution_string).
    """
    critical = log_b(a, b)

    # Compare f(n) = n^d * log^k n against n^critical.
    if fn_degree < critical - 1e-9:
        case = 1
    elif abs(fn_degree - critical) < 1e-9:
        case = 2
    else:
        # Regularity condition: a * f(n/b) <= c * f(n) for c < 1.
        # For f(n) = n^d log^k n it holds whenever d > 0 (or d == 0 and k... use d > critical).
        # Here fn_degree > critical >= 0, so a*(n/b)^d = (a/b^d) * n^d
        # and a/b^d < 1 because d > log_b a. Regularity satisfied.
        case = 3

    poly = f"n^{critical:.4g}" if abs(critical - round(critical)) > 1e-9 else f"n^{int(round(critical))}"

    if case == 1:
        return case, f"Theta({poly})"
    if case == 2:
        if fn_log_power == 0:
            return case, f"Theta({poly} * log n)"
        return case, f"Theta({poly} * log^{fn_log_power + 1} n)"
    f_str = f"n^{fn_degree}"
    if fn_log_power:
        f_str += f" * log^{fn_log_power} n"
    return case, f"Theta({f_str})"


if __name__ == "__main__":
    # Hardcoded input: list of recurrences (a, b, degree of f(n), log power of f(n), label)
    recurrences = [
        (2, 2, 1, 0, "T(n) = 2T(n/2) + n          [Merge Sort]"),
        (2, 2, 0, 0, "T(n) = 2T(n/2) + 1          [Binary Search style]"),
        (1, 2, 1, 0, "T(n) = T(n/2) + n"),
        (4, 2, 2, 0, "T(n) = 4T(n/2) + n^2"),
        (7, 2, 2, 0, "T(n) = 7T(n/2) + n^2        [Strassen]"),
        (3, 2, 2, 0, "T(n) = 3T(n/2) + n^2        [Karatsuba]"),
        (2, 2, 1, 1, "T(n) = 2T(n/2) + n log n"),
        (2, 4, 1, 0, "T(n) = 2T(n/4) + n"),
    ]

    print(f"{'Recurrence':<45} {'log_b(a)':>9} {'Case':>5}  Solution")
    print("-" * 95)
    for a, b, d, k, label in recurrences:
        case, solution = master_method(a, b, d, k)
        print(f"{label:<45} {log_b(a, b):>9.3f} {case:>5}  {solution}")
