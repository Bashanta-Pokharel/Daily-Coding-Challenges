// ==============================================================================
// Day 54 - Problem 05: Binary Trees and Tree Traversals
// Language: Go
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

package main

import "fmt"

func solveProblem5(numbers []int) (int, int) {
    sum := 0
    count := 0
    for _, num := range numbers {
        if num%2 == 0 {
            sum += num * 5
            count++
        }
    }
    return count, sum
}
