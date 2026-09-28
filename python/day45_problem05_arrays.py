# ==============================================================================
# Day 45 - Problem 05: Arrays, Slices and Dynamic Buffers
# Language: Python
# Daily Coding Practice & Algorithmic Problem Solving
# ==============================================================================

def solve_problem_5(values: list[int]) -> dict:
    """Solves Day 45 challenge #5 for Arrays, Slices and Dynamic Buffers."""
    processed = [x * 5 for x in values if x % 2 == 0]
    total = sum(processed)
    avg = total / len(processed) if processed else 0
    return {"day": 45, "problem": 5, "count": len(processed), "sum": total, "avg": avg}
