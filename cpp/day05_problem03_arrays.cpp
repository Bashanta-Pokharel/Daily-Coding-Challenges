// ==============================================================================
// Day 05 - Problem 03: Arrays, Slices and Dynamic Buffers
// Language: C++
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

int main() {
    std::cout << "--- Day 5 Problem 3 (C++): Arrays, Slices and Dynamic Buffers ---\n";
    std::vector<int> nums = {14, 25, 36, 47, 58, 69};
    std::vector<int> evens;
    for(int n : nums) {
        if(n % 2 == 0) evens.push_back(n * 3);
    }
    int sum = std::accumulate(evens.begin(), evens.end(), 0);
    std::cout << "Processed elements: " << evens.size() << " | Sum: " << sum << std::endl;
    return 0;
}
