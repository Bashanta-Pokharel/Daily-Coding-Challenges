// ==============================================================================
// Day 51 - Problem 03: Sorting Algorithms and Heuristics
// Language: Java
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Day51_Problem03_sorting_algorithms_and_heuristics {
    public static void main(String[] args) {
        System.out.println("--- Day 51 Problem 3 (Java): Sorting Algorithms and Heuristics ---");
        List<Integer> numbers = Arrays.asList(12, 23, 34, 45, 56, 67);
        List<Integer> evens = numbers.stream().filter(n -> n % 2 == 0).map(n -> n * 3).collect(Collectors.toList());
        int sum = evens.stream().mapToInt(Integer::intValue).sum();
        boolean verified = !evens.isEmpty() && sum > 0;
        System.out.println("Result List: " + evens + " | Sum: " + sum);
        System.out.println("Verification passed: " + verified);
    }
}

// Complexity: O(N) time, O(N) space
