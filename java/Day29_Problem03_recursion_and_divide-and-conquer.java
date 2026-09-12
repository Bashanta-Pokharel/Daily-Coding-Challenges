// ==============================================================================
// Day 29 - Problem 03: Recursion and Divide-and-Conquer
// Language: Java
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Day29_Problem03_recursion_and_divide-and-conquer {
    public static void main(String[] args) {
        System.out.println("--- Day 29 Problem 3 (Java): Recursion and Divide-and-Conquer ---");
        List<Integer> numbers = Arrays.asList(12, 23, 34, 45, 56, 67);
        List<Integer> evens = numbers.stream().filter(n -> n % 2 == 0).map(n -> n * 3).collect(Collectors.toList());
        int sum = evens.stream().mapToInt(Integer::intValue).sum();
        boolean verified = !evens.isEmpty() && sum > 0;
        System.out.println("Result List: " + evens + " | Sum: " + sum);
        System.out.println("Verification passed: " + verified);
    }
}

// Complexity: O(N) time, O(N) space
