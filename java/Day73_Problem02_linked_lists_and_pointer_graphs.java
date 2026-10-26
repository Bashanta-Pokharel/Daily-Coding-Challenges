// ==============================================================================
// Day 73 - Problem 02: Linked Lists and Pointer Graphs
// Language: Java
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Day73_Problem02_linked_lists_and_pointer_graphs {
    public static void main(String[] args) {
        System.out.println("--- Day 73 Problem 2 (Java): Linked Lists and Pointer Graphs ---");
        List<Integer> numbers = Arrays.asList(12, 23, 34, 45, 56, 67);
        List<Integer> evens = numbers.stream().filter(n -> n % 2 == 0).map(n -> n * 2).collect(Collectors.toList());
        int sum = evens.stream().mapToInt(Integer::intValue).sum();
        boolean verified = !evens.isEmpty() && sum > 0;
        System.out.println("Result List: " + evens + " | Sum: " + sum);
        System.out.println("Verification passed: " + verified);
    }
}

// Complexity: O(N) time, O(N) space
