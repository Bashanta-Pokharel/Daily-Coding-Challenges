// ==============================================================================
// Day 77 - Problem 05: Bitwise Manipulation and Masking
// Language: Rust
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

fn main() {
    println!("--- Day {} Problem {} (Rust): {} ---", 77, 5, "Bitwise Manipulation and Masking");
    let data = vec![10, 21, 32, 43, 54, 65];
    let evens: Vec<i32> = data.into_iter().filter(|x| x % 2 == 0).map(|x| x * 5).collect();
    let sum: i32 = evens.iter().sum();
    let verified = !evens.is_empty() && sum > 0;
    println!("Evens: {:?}, Sum: {}", evens, sum);
    println!("Verification passed: {}", verified);
}

// Time: O(N), Space: O(N)
