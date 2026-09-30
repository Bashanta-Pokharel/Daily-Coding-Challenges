// ==============================================================================
// Day 47 - Problem 02: Hash Maps and Lookup Tables
// Language: TypeScript
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

function solveProblem2(inputArray) {
  const filtered = inputArray.filter(n => n % 2 === 0).map(n => n * 2);
  const sum = filtered.reduce((acc, curr) => acc + curr, 0);
  return { day: 47, problem: 2, items: filtered, total: sum };
}
