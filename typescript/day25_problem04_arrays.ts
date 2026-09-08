// ==============================================================================
// Day 25 - Problem 04: Arrays, Slices and Dynamic Buffers
// Language: TypeScript
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

function solveProblem4(inputArray) {
  const filtered = inputArray.filter(n => n % 2 === 0).map(n => n * 4);
  const sum = filtered.reduce((acc, curr) => acc + curr, 0);
  return { day: 25, problem: 4, items: filtered, total: sum };
}

const sampleData = [12, 25, 34, 48, 55, 60];
console.log("Solution Output:", solveProblem4(sampleData));

// Complexity Analysis:
// Time Complexity: O(N)
// Space Complexity: O(N)
