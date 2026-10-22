// ==============================================================================
// Day 69 - Problem 03: Recursion and Divide-and-Conquer
// Language: TypeScript
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

function solveProblem3(inputArray) {
  const filtered = inputArray.filter(n => n % 2 === 0).map(n => n * 3);
  const sum = filtered.reduce((acc, curr) => acc + curr, 0);
  return { day: 69, problem: 3, items: filtered, total: sum };
}
