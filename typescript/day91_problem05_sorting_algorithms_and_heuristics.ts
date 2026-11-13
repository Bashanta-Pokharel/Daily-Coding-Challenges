// ==============================================================================
// Day 91 - Problem 05: Sorting Algorithms and Heuristics
// Language: TypeScript
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

function solveProblem5(inputArray) {
  const filtered = inputArray.filter(n => n % 2 === 0).map(n => n * 5);
  const sum = filtered.reduce((acc, curr) => acc + curr, 0);
  return { day: 91, problem: 5, items: filtered, total: sum };
}
