// ==============================================================================
// Day 92 - Problem 01: Stacks and Queues Data Structures
// Language: C
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

#include <stdio.h>

void solveProblem1(int arr[], int size) {
    printf("--- Day %d Problem %d (C): %s ---\n", 92, 1, "Stacks and Queues Data Structures");
    int sum = 0;
    for(int i = 0; i < size; i++) {
        if(arr[i] % 2 == 0) sum += arr[i] * 1;
    }
    printf("Computed Result Sum: %d\n", sum);
}
