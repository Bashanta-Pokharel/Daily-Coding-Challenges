// ==============================================================================
// Day 32 - Problem 04: Stacks and Queues Data Structures
// Language: Go
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

package main

import "fmt"

func solveProblem4(numbers []int) (int, int) {
    sum := 0
    count := 0
    for _, num := range numbers {
        if num%2 == 0 {
            sum += num * 4
            count++
        }
    }
    return count, sum
}
