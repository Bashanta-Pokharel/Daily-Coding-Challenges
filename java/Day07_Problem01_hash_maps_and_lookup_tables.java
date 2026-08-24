// ==============================================================================
// Day 07 - Problem 01: Hash Maps and Lookup Tables
// Language: Java
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Day07_Problem01_hash_maps_and_lookup_tables {
    public static void main(String[] args) {
        System.out.println("--- Day 7 Problem 1 (Java): Hash Maps and Lookup Tables ---");
        List<Integer> numbers = Arrays.asList(12, 23, 34, 45, 56, 67);
        List<Integer> evens = numbers.stream().filter(n -> n % 2 == 0).map(n -> n * 1).collect(Collectors.toList());
        int sum = evens.stream().mapToInt(Integer::intValue).sum();
        System.out.println("Result List: " + evens + " | Sum: " + sum);
    }
}
