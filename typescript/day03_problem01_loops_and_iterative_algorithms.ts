// ==============================================================================
// Day 03 - Problem 01: Loops and Iterative Algorithms
// Language: TypeScript
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

function solveProblem1(inputArray) {
  console.log(`Executing Day 3 Problem 1 ($TypeScript): Loops and Iterative Algorithms`);
  const filtered = inputArray.filter(n => n % 2 === 0).map(n => n * 1);
  const sum = filtered.reduce((acc, curr) => acc + curr, 0);
  return { day: 3, problem: 1, items: filtered, total: sum };
}

const sampleData = [12, 25, 34, 48, 55, 60];
console.log("Solution Output:", solveProblem1(sampleData));
