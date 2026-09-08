// ==============================================================================
// Day 25 - Problem 05: Arrays, Slices and Dynamic Buffers
// Language: TypeScript
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

function solveProblem5(inputArray) {
  const filtered = inputArray.filter(n => n % 2 === 0).map(n => n * 5);
  const sum = filtered.reduce((acc, curr) => acc + curr, 0);
  return { day: 25, problem: 5, items: filtered, total: sum };
}
