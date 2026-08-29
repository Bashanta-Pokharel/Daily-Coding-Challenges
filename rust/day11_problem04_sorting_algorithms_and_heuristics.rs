// ==============================================================================
// Day 11 - Problem 04: Sorting Algorithms and Heuristics
// Language: Rust
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

fn main() {
    println!("--- Day {} Problem {} (Rust): {} ---", 11, 4, "Sorting Algorithms and Heuristics");
    let data = vec![10, 21, 32, 43, 54, 65];
    let evens: Vec<i32> = data.into_iter().filter(|x| x % 2 == 0).map(|x| x * 4).collect();
    let sum: i32 = evens.iter().sum();
    println!("Evens: {:?}, Sum: {}", evens, sum);
}
