// ==============================================================================
// Day 48 - Problem 03: Object-Oriented and Structural Design
// Language: C
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

#include <stdio.h>

void solveProblem3(int arr[], int size) {
    printf("--- Day %d Problem %d (C): %s ---\n", 48, 3, "Object-Oriented and Structural Design");
    int sum = 0;
    for(int i = 0; i < size; i++) {
        if(arr[i] % 2 == 0) sum += arr[i] * 3;
    }
    printf("Computed Result Sum: %d\n", sum);
}
