// ==============================================================================
// Day 70 - Problem 05: Binary Search and Sliding Windows
// Language: C
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

#include <stdio.h>

void solveProblem5(int arr[], int size) {
    printf("--- Day %d Problem %d (C): %s ---\n", 70, 5, "Binary Search and Sliding Windows");
    int sum = 0;
    for(int i = 0; i < size; i++) {
        if(arr[i] % 2 == 0) sum += arr[i] * 5;
    }
    printf("Computed Result Sum: %d\n", sum);
}
