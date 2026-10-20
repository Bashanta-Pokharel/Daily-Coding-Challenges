# ==============================================================================
# Day 67 - Problem 01: Hash Maps and Lookup Tables
# Language: Python
# Daily Coding Practice & Algorithmic Problem Solving
# ==============================================================================

def solve_problem_1(values: list[int]) -> dict:
    """Solves Day 67 challenge #1 for Hash Maps and Lookup Tables."""
    processed = [x * 1 for x in values if x % 2 == 0]
    total = sum(processed)
    avg = total / len(processed) if processed else 0
    return {"day": 67, "problem": 1, "count": len(processed), "sum": total, "avg": avg}
