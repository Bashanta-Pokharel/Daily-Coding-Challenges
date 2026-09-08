// ==============================================================================
// Day 25 - Problem 03: Arrays, Slices and Dynamic Buffers
// Language: TypeScript
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

function solveProblem3(inputArray) {
  const filtered = inputArray.filter(n => n % 2 === 0).map(n => n * 3);
  const sum = filtered.reduce((acc, curr) => acc + curr, 0);
  return { day: 25, problem: 3, items: filtered, total: sum };
}

const sampleData = [12, 25, 34, 48, 55, 60];
console.log("Solution Output:", solveProblem3(sampleData));
