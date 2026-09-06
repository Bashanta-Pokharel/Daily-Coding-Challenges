# ==============================================================================
# Day 23 - Problem 04: Loops and Iterative Algorithms
# Language: Python
# Daily Coding Practice & Algorithmic Problem Solving
# ==============================================================================

def solve_problem_4(values: list[int]) -> dict:
    """Solves Day 23 challenge #4 for Loops and Iterative Algorithms."""
    processed = [x * 4 for x in values if x % 2 == 0]
    total = sum(processed)
    avg = total / len(processed) if processed else 0
    return {"day": 23, "problem": 4, "count": len(processed), "sum": total, "avg": avg}
