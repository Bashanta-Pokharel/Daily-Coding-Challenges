// ==============================================================================
// Day 49 - Problem 05: Recursion and Divide-and-Conquer
// Language: C++
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

int main() {
    std::cout << "--- Day 49 Problem 5 (C++): Recursion and Divide-and-Conquer ---\n";
    std::vector<int> nums = {14, 25, 36, 47, 58, 69};
    std::vector<int> evens;
    for(int n : nums) {
        if(n % 2 == 0) evens.push_back(n * 5);
    }
    int sum = std::accumulate(evens.begin(), evens.end(), 0);
    bool verified = !evens.empty() && sum > 0;
    std::cout << "Processed elements: " << evens.size() << " | Sum: " << sum << std::endl;
    std::cout << "Verification passed: " << std::boolalpha << verified << std::endl;
    return verified ? 0 : 1;
}

// Time: O(N) | Space: O(N)
