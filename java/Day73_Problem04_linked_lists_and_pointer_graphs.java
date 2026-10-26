// ==============================================================================
// Day 73 - Problem 04: Linked Lists and Pointer Graphs
// Language: Java
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Day73_Problem04_linked_lists_and_pointer_graphs {
    public static void main(String[] args) {
        System.out.println("--- Day 73 Problem 4 (Java): Linked Lists and Pointer Graphs ---");
        List<Integer> numbers = Arrays.asList(12, 23, 34, 45, 56, 67);
        List<Integer> evens = numbers.stream().filter(n -> n % 2 == 0).map(n -> n * 4).collect(Collectors.toList());
        int sum = evens.stream().mapToInt(Integer::intValue).sum();
        System.out.println("Result List: " + evens + " | Sum: " + sum);
    }
}
