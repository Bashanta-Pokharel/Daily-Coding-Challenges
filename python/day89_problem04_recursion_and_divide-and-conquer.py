# ==============================================================================
# Day 89 - Problem 04: Recursion and Divide-and-Conquer
# Language: Python
# Daily Coding Practice & Algorithmic Problem Solving
# ==============================================================================

def solve_problem_4(values: list[int]) -> dict:
    """Solves Day 89 challenge #4 for Recursion and Divide-and-Conquer."""
    processed = [x * 4 for x in values if x % 2 == 0]
    total = sum(processed)
    avg = total / len(processed) if processed else 0
    return {"day": 89, "problem": 4, "count": len(processed), "sum": total, "avg": avg}
