// ==============================================================================
// Day 95 - Problem 03: Graph Algorithms BFS and DFS
// Language: Java
// Daily Coding Practice & Algorithmic Problem Solving
// ==============================================================================

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Day95_Problem03_graph_algorithms_bfs_and_dfs {
    public static void main(String[] args) {
        System.out.println("--- Day 95 Problem 3 (Java): Graph Algorithms BFS and DFS ---");
        List<Integer> numbers = Arrays.asList(12, 23, 34, 45, 56, 67);
        List<Integer> evens = numbers.stream().filter(n -> n % 2 == 0).map(n -> n * 3).collect(Collectors.toList());
        int sum = evens.stream().mapToInt(Integer::intValue).sum();
        System.out.println("Result List: " + evens + " | Sum: " + sum);
    }
}
