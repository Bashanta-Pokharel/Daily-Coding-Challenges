// ==============================================================================
// Day 04 - Problem 03: Functions, Closures and Lambdas
// Language: C
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

#include <stdio.h>

void solveProblem3(int arr[], int size) {
    printf("--- Day %d Problem %d (C): %s ---\n", 4, 3, "Functions, Closures and Lambdas");
    int sum = 0;
    for(int i = 0; i < size; i++) {
        if(arr[i] % 2 == 0) {
            sum += arr[i] * 3;
        }
    }
    printf("Computed Result Sum: %d\n", sum);
}

int main(void) {
    int dataset[] = {10, 21, 32, 43, 54, 65};
    solveProblem3(dataset, sizeof(dataset)/sizeof(dataset[0]));
    return 0;
}
