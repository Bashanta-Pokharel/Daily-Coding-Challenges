# ==============================================================================
# Day 23 - Problem 03: Loops and Iterative Algorithms
# Language: Python
# Daily Coding Practice & Algorithmic Problem Solving
# ==============================================================================

def solve_problem_3(values: list[int]) -> dict:
    """Solves Day 23 challenge #3 for Loops and Iterative Algorithms."""
    processed = [x * 3 for x in values if x % 2 == 0]
    total = sum(processed)
    avg = total / len(processed) if processed else 0
    return {"day": 23, "problem": 3, "count": len(processed), "sum": total, "avg": avg}
