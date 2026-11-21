// ==============================================================================
// Day 99 - Problem 02: File IO and Data Serialization
// Language: Rust
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

fn main() {
    println!("--- Day {} Problem {} (Rust): {} ---", 99, 2, "File IO and Data Serialization");
    let data = vec![10, 21, 32, 43, 54, 65];
    let evens: Vec<i32> = data.into_iter().filter(|x| x % 2 == 0).map(|x| x * 2).collect();
    let sum: i32 = evens.iter().sum();
    println!("Evens: {:?}, Sum: {}", evens, sum);
}
