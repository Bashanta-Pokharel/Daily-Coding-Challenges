// ==============================================================================
// Day 47 - Problem 04: Hash Maps and Lookup Tables
// Language: TypeScript
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

function solveProblem4(inputArray) {
  const filtered = inputArray.filter(n => n % 2 === 0).map(n => n * 4);
  const sum = filtered.reduce((acc, curr) => acc + curr, 0);
  return { day: 47, problem: 4, items: filtered, total: sum };
}
