// ==============================================================================
// Day 68 - Problem 01: Object-Oriented and Structural Design
// Language: JavaScript
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

function solveProblem1(inputArray) {
  const filtered = inputArray.filter(n => n % 2 === 0).map(n => n * 1);
  const sum = filtered.reduce((acc, curr) => acc + curr, 0);
  return { day: 68, problem: 1, items: filtered, total: sum };
}
