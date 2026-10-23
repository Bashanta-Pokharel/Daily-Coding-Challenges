// ==============================================================================
// Day 70 - Problem 03: Binary Search and Sliding Windows
// Language: C
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

#include <stdio.h>

void solveProblem3(int arr[], int size) {
    printf("--- Day %d Problem %d (C): %s ---\n", 70, 3, "Binary Search and Sliding Windows");
    int sum = 0;
    for(int i = 0; i < size; i++) {
        if(arr[i] % 2 == 0) sum += arr[i] * 3;
    }
    printf("Computed Result Sum: %d\n", sum);
}

int main(void) {
    int dataset[] = {10, 21, 32, 43, 54, 65};
    solveProblem3(dataset, sizeof(dataset)/sizeof(dataset[0]));
    return 0;
}
