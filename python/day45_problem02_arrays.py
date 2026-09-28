# ==============================================================================
# Day 45 - Problem 02: Arrays, Slices and Dynamic Buffers
# Language: Python
# Daily Coding Practice & Algorithmic Problem Solving
# ==============================================================================

def solve_problem_2(values: list[int]) -> dict:
    """Solves Day 45 challenge #2 for Arrays, Slices and Dynamic Buffers."""
    processed = [x * 2 for x in values if x % 2 == 0]
    total = sum(processed)
    avg = total / len(processed) if processed else 0
    return {"day": 45, "problem": 2, "count": len(processed), "sum": total, "avg": avg}
