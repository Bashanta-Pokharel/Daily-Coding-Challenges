// ==============================================================================
// Day 71 - Problem 01: Sorting Algorithms and Heuristics
// Language: C++
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

int main() {
    std::cout << "--- Day 71 Problem 1 (C++): Sorting Algorithms and Heuristics ---\n";
    std::vector<int> nums = {14, 25, 36, 47, 58, 69};
    std::vector<int> evens;
    for(int n : nums) {
        if(n % 2 == 0) evens.push_back(n * 1);
    }
    int sum = std::accumulate(evens.begin(), evens.end(), 0);
    bool verified = !evens.empty() && sum > 0;
    std::cout << "Processed elements: " << evens.size() << " | Sum: " << sum << std::endl;
    std::cout << "Verification passed: " << std::boolalpha << verified << std::endl;
    return verified ? 0 : 1;
}

// Time: O(N) | Space: O(N)
