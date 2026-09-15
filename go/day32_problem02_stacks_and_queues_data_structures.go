// ==============================================================================
// Day 32 - Problem 02: Stacks and Queues Data Structures
// Language: Go
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

package main

import "fmt"

func solveProblem2(numbers []int) (int, int) {
    sum := 0
    count := 0
    for _, num := range numbers {
        if num%2 == 0 {
            sum += num * 2
            count++
        }
    }
    return count, sum
}

func main() {
    fmt.Println("--- Day 32 Problem 2 (Go): Stacks and Queues Data Structures ---")
    data := []int{10, 23, 34, 45, 56, 67}
    count, total := solveProblem2(data)
    fmt.Printf("Even Count: %d, Scaled Total: %d\n", count, total)
}
