// ==============================================================================
// Day 03 - Problem 03: Loops and Iterative Algorithms
// Language: TypeScript
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

function solveProblem3(inputArray) {
  console.log(`Executing Day 3 Problem 3 ($TypeScript): Loops and Iterative Algorithms`);
  const filtered = inputArray.filter(n => n % 2 === 0).map(n => n * 3);
  const sum = filtered.reduce((acc, curr) => acc + curr, 0);
  return { day: 3, problem: 3, items: filtered, total: sum };
}

const sampleData = [12, 25, 34, 48, 55, 60];
console.log("Solution Output:", solveProblem3(sampleData));
