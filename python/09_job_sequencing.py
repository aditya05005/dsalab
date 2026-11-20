# Job Sequencing with Deadlines - Greedy Algorithm.
# Each job takes 1 unit of time, gives a profit, and must finish by its deadline.
# Greedy: sort jobs by profit (descending); schedule each job in the latest
# free slot <= its deadline. Optimal for the unit-time case.
# Complexity: O(n^2) with slot array (O(n log n) achievable with DSU).


def job_sequencing(jobs):
    """jobs: list of (name, profit, deadline). Returns (schedule, total_profit)."""
    jobs = sorted(jobs, key=lambda j: j[1], reverse=True)
    max_deadline = max(deadline for _, _, deadline in jobs)
    slots = [None] * (max_deadline + 1)  # index = time slot 1..max_deadline
    total = 0
    for name, profit, deadline in jobs:
        for t in range(min(deadline, max_deadline), 0, -1):
            if slots[t] is None:
                slots[t] = (name, profit)
                total += profit
                break
    return [s for s in slots[1:] if s is not None], total


if __name__ == "__main__":
    # Hardcoded input: (job_id, profit, deadline)
    jobs = [("J1", 100, 2),
            ("J2", 19, 1),
            ("J3", 27, 2),
            ("J4", 25, 1),
            ("J5", 15, 3)]

    print("Jobs (id, profit, deadline):")
    for name, profit, deadline in jobs:
        print(f"  {name}: profit={profit:>3}, deadline={deadline}")
    print("Each job takes 1 unit of time.\n")

    schedule, total = job_sequencing(jobs)

    print("Greedy schedule (sorted by profit, latest free slot first):")
    for t, (name, profit) in enumerate(schedule, start=1):
        print(f"  time slot {t}: {name} (profit {profit})")

    print(f"\nTotal profit = {total}")
    print("Analysis: sorting O(n log n) + slot scan O(n * max_deadline) => O(n^2).")
