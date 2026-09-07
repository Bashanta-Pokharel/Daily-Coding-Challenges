// ==============================================================================
// Day 24 - Problem 05: Functions, Closures and Lambdas
// Language: JavaScript
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

function solveProblem5(inputArray) {
  const filtered = inputArray.filter(n => n % 2 === 0).map(n => n * 5);
  const sum = filtered.reduce((acc, curr) => acc + curr, 0);
  return { day: 24, problem: 5, items: filtered, total: sum };
}

const sampleData = [12, 25, 34, 48, 55, 60];
console.log("Solution Output:", solveProblem5(sampleData));
