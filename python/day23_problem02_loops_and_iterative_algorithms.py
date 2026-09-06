# ==============================================================================
# Day 23 - Problem 02: Loops and Iterative Algorithms
# Language: Python
# Daily Coding Practice & Algorithmic Problem Solving
# ==============================================================================

def solve_problem_2(values: list[int]) -> dict:
    """Solves Day 23 challenge #2 for Loops and Iterative Algorithms."""
    processed = [x * 2 for x in values if x % 2 == 0]
    total = sum(processed)
    avg = total / len(processed) if processed else 0
    return {"day": 23, "problem": 2, "count": len(processed), "sum": total, "avg": avg}
