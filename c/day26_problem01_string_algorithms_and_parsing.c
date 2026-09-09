// ==============================================================================
// Day 26 - Problem 01: String Algorithms and Parsing
// Language: C
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

#include <stdio.h>

void solveProblem1(int arr[], int size) {
    printf("--- Day %d Problem %d (C): %s ---\n", 26, 1, "String Algorithms and Parsing");
    int sum = 0;
    for(int i = 0; i < size; i++) {
        if(arr[i] % 2 == 0) sum += arr[i] * 1;
    }
    printf("Computed Result Sum: %d\n", sum);
}

int main(void) {
    int dataset[] = {10, 21, 32, 43, 54, 65};
    solveProblem1(dataset, sizeof(dataset)/sizeof(dataset[0]));
    return 0;
}
