#!/usr/bin/env python3
"""
Automated Multi-Language Daily Code Generator
Generates 2 educational coding problems & solutions every day across ALL major
programming languages in the software industry, creating 3 individual commits daily.
"""

import os
import sys
import json
import subprocess
from datetime import datetime, date

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
STATE_FILE = os.path.join(WORKSPACE_DIR, "scripts", ".daily_state.json")
README_FILE = os.path.join(WORKSPACE_DIR, "README.md")

# Complete catalog of top industry & market programming languages
LANGUAGE_CONFIG = {
    "python": {"ext": "py", "comment": "#", "display": "Python"},
    "javascript": {"ext": "js", "comment": "//", "display": "JavaScript (ES6+)"},
    "typescript": {"ext": "ts", "comment": "//", "display": "TypeScript"},
    "c": {"ext": "c", "comment": "//", "display": "C (C99/C11)"},
    "cpp": {"ext": "cpp", "comment": "//", "display": "C++ (Modern C++17/20)"},
    "csharp": {"ext": "cs", "comment": "//", "display": "C# (.NET)"},
    "java": {"ext": "java", "comment": "//", "display": "Java (17+)"},
    "kotlin": {"ext": "kt", "comment": "//", "display": "Kotlin"},
    "swift": {"ext": "swift", "comment": "//", "display": "Swift"},
    "go": {"ext": "go", "comment": "//", "display": "Go (Golang)"},
    "rust": {"ext": "rs", "comment": "//", "display": "Rust"},
    "php": {"ext": "php", "comment": "//", "display": "PHP 8+"},
    "ruby": {"ext": "rb", "comment": "#", "display": "Ruby"},
    "dart": {"ext": "dart", "comment": "//", "display": "Dart (Flutter)"},
    "scala": {"ext": "scala", "comment": "//", "display": "Scala"},
    "r": {"ext": "r", "comment": "#", "display": "R (Data Science)"},
    "bash": {"ext": "sh", "comment": "#", "display": "Bash / Shell Scripting"},
    "sql": {"ext": "sql", "comment": "--", "display": "SQL"},
    "lua": {"ext": "lua", "comment": "--", "display": "Lua"},
    "julia": {"ext": "jl", "comment": "#", "display": "Julia"},
    "haskell": {"ext": "hs", "comment": "--", "display": "Haskell"},
    "elixir": {"ext": "ex", "comment": "#", "display": "Elixir"}
}

LANGUAGES = list(LANGUAGE_CONFIG.keys())

# Comprehensive Topic Matrix
TOPICS = [
    ("Variables, Primitive Data Types & Type Systems", "fundamentals"),
    ("Conditionals, Pattern Matching & Control Flow", "control_flow"),
    ("Loops, Iteration & Stream Processing", "loops"),
    ("Functions, Lambdas & First-Class Citizens", "functions"),
    ("Arrays, Slices & Dynamic Lists", "arrays"),
    ("String Manipulation, Unicode & Regular Expressions", "strings"),
    ("Hash Maps, Dictionaries & Key-Value Stores", "hashmaps"),
    ("Object-Oriented Programming, Encapsulation & Polymorphism", "oop"),
    ("Recursion, Backtracking & Divide-and-Conquer", "recursion"),
    ("Binary Search & Two-Pointer Algorithms", "search_algorithms"),
    ("Sorting Algorithms (QuickSort, MergeSort, HeapSort)", "sorting"),
    ("Stack & Queue Linear Data Structures", "stacks_queues"),
    ("Linked Lists (Singly, Doubly & Circular)", "linked_lists"),
    ("Binary Trees, BST & Tree Traversals", "trees"),
    ("Graph Traversals (BFS, DFS & Shortest Path)", "graphs"),
    ("Dynamic Programming & Memoization", "dp"),
    ("Bitwise Manipulation & Low-Level Operations", "bitwise"),
    ("Concurrency, Multithreading & Asynchronous Tasks", "concurrency"),
    ("File I/O, Serialization & JSON Parsing", "io_parsing"),
    ("Error Handling, Optionals & Result Types", "error_handling")
]

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {"current_day": 1, "lang_index": 0, "history": []}

def save_state(state):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def run_git(args):
    try:
        subprocess.run(["git"] + args, cwd=WORKSPACE_DIR, check=False)
    except Exception as e:
        print(f"Git command notice: {e}")

def generate_code_content(lang: str, day: int, problem_num: int, topic: str) -> tuple[str, str]:
    cfg = LANGUAGE_CONFIG[lang]
    ext = cfg["ext"]
    disp = cfg["display"]
    cmt = cfg["comment"]
    
    clean_topic = topic.split(",")[0].lower().replace(" ", "_").replace("&", "and")
    filename = f"day{day:02d}_{problem_num:02d}_{clean_topic}_{problem_num}.{ext}"
    
    header = f"""{cmt} ==============================================================================
{cmt} Day {day:02d} - Problem {problem_num:02d}: {topic}
{cmt} Language: {disp}
{cmt} Automated Problem Solving & Daily Practice
{cmt} ==============================================================================
"""

    # Language-specific idiomatic code templates
    if lang == "python":
        if problem_num == 1:
            code = f"""{header}
def solve_problem_1():
    print("--- Day {day} Problem 1 ({disp}): {topic} ---")
    data = [i * {day} for i in range(1, 8)]
    processed = [x ** 2 for x in data if x % 2 == 0]
    print(f"Initial Dataset: {{data}}")
    print(f"Transformed Result: {{processed}}")
    return processed

if __name__ == "__main__":
    solve_problem_1()
"""
        else:
            code = f"""{header}
class SolutionDay{day}:
    def __init__(self, name: str = "{disp} Practitioner"):
        self.name = name
        self.day = {day}

    def execute_algorithm(self, values: list[int]) -> dict:
        total = sum(values)
        avg = total / len(values) if values else 0
        return {{"day": self.day, "count": len(values), "sum": total, "avg": avg}}

if __name__ == "__main__":
    solver = SolutionDay{day}()
    res = solver.execute_algorithm([10, 25, 30, 45, 60, 85])
    print(f"Algorithm Output: {{res}}")
"""

    elif lang in ("javascript", "typescript"):
        code = f"""{header}
function solveDay{day}Problem{problem_num}() {{
  console.log(`--- Day {day} Problem {problem_num} (${disp}): {topic} ---`);
  const dataset = Array.from({{ length: 6 }}, (_, i) => (i + 1) * {day});
  const results = dataset.map(n => ({{ original: n, processed: n * 2 + {problem_num} }}));
  console.table(results);
  return results;
}}

solveDay{day}Problem{problem_num}();
"""

    elif lang == "c":
        code = f"""{header}
#include <stdio.h>

void executeDay{day}Problem{problem_num}(void) {{
    printf("--- Day %d Problem %d ({disp}): %s ---\\n", {day}, {problem_num}, "{topic}");
    int data[] = {{10, 20, 30, 40, 50}};
    size_t count = sizeof(data) / sizeof(data[0]);
    int sum = 0;
    for(size_t i = 0; i < count; i++) {{
        sum += data[i] * {problem_num};
    }}
    printf("Computed Aggregation: %d\\n", sum);
}}

int main(void) {{
    executeDay{day}Problem{problem_num}();
    return 0;
}}
"""

    elif lang == "cpp":
        code = f"""{header}
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

int main() {{
    std::cout << "--- Day {day} Problem {problem_num} ({disp}): {topic} ---\\n";
    std::vector<int> numbers = {{5 * {day}, 12 * {day}, 18 * {day}, 25 * {day}}};
    int total = std::accumulate(numbers.begin(), numbers.end(), 0);
    std::cout << "Element Count: " << numbers.size() << ", Sum: " << total << std::endl;
    return 0;
}}
"""

    elif lang == "csharp":
        code = f"""{header}
using System;
using System.Linq;
using System.Collections.Generic;

namespace DailyCodeChallenge
{{
    class Program
    {{
        static void Main(string[] args)
        {{
            Console.WriteLine("--- Day {day} Problem {problem_num} ({disp}): {topic} ---");
            var numbers = new List<int> {{ 10, 20, 30, 40, 50 }};
            var squaredEvens = numbers.Where(n => n % 2 == 0).Select(n => n * {day}).ToList();
            Console.WriteLine($"Result Count: {{squaredEvens.Count}}, Sum: {{squaredEvens.Sum()}}");
        }}
    }}
}}
"""

    elif lang == "java":
        classname = f"Day{day:02d}_{problem_num:02d}_{clean_topic}"
        filename = f"{classname}.java"
        code = f"""{header}
import java.util.Arrays;
import java.util.List;

public class {classname} {{
    public static void main(String[] args) {{
        System.out.println("--- Day {day} Problem {problem_num} ({disp}): {topic} ---");
        List<Integer> list = Arrays.asList(15 * {day}, 28 * {day}, 42 * {day}, 56 * {day});
        int sum = list.stream().mapToInt(Integer::intValue).sum();
        System.out.println("List: " + list + " | Total: " + sum);
    }}
}}
"""

    elif lang == "go":
        code = f"""{header}
package main

import "fmt"

func main() {{
    fmt.Printf("--- Day %d Problem %d ({disp}): %s ---\\n", {day}, {problem_num}, "{topic}")
    items := []int{{10 * {day}, 20 * {day}, 30 * {day}, 40 * {day}}}
    total := 0
    for _, val := range items {{
        total += val
    }}
    fmt.Printf("Items: %v | Calculated Sum: %d\\n", items, total)
}}
"""

    elif lang == "rust":
        code = f"""{header}
fn main() {{
    println!("--- Day {} Problem {} ({disp}): {} ---", {day}, {problem_num}, "{topic}");
    let values: Vec<i32> = (1..=5).map(|x| x * {day} * {problem_num}).collect();
    let sum: i32 = values.iter().sum();
    println!("Vector: {:?}, Sum: {}", values, sum);
}}
"""

    elif lang == "kotlin":
        code = f"""{header}
fun main() {{
    println("--- Day {day} Problem {problem_num} ({disp}): {topic} ---")
    val items = listOf(10 * {day}, 25 * {day}, 30 * {day})
    val total = items.sum()
    println("Items: $items -> Sum: $total")
}}
"""

    elif lang == "swift":
        code = f"""{header}
import Foundation

print("--- Day {day} Problem {problem_num} ({disp}): {topic} ---")
let numbers = [5 * {day}, 15 * {day}, 25 * {day}, 35 * {day}]
let sum = numbers.reduce(0, +)
print("Array: \\(numbers), Sum: \\(sum)")
"""

    elif lang == "php":
        code = f"""<?php
{header}
echo "--- Day {day} Problem {problem_num} ({disp}): {topic} ---\\n";
$data = array_map(fn($n) => $n * {day}, [2, 4, 6, 8, 10]);
$sum = array_sum($data);
echo "Data: " . implode(", ", $data) . " | Sum: " . $sum . "\\n";
"""

    elif lang == "ruby":
        code = f"""{header}
puts "--- Day {day} Problem {problem_num} ({disp}): {topic} ---"
numbers = (1..6).map {{ |x| x * {day} }}
puts "Numbers: #{{numbers.inspect}}"
puts "Sum: #{{numbers.sum}}"
"""

    elif lang == "dart":
        code = f"""{header}
void main() {{
  print('--- Day {day} Problem {problem_num} ({disp}): {topic} ---');
  final nums = [10 * {day}, 20 * {day}, 30 * {day}];
  final sum = nums.reduce((a, b) => a + b);
  print('Dart List: $nums | Total: $sum');
}}
"""

    elif lang == "scala":
        code = f"""{header}
object Day{day}Problem{problem_num} extends App {{
  println(s"--- Day {day} Problem {problem_num} ({disp}): {topic} ---")
  val numbers = List(5, 10, 15, 20).map(_ * {day})
  println(s"Numbers: $numbers | Sum: ${{numbers.sum}}")
}}
"""

    elif lang == "r":
        code = f"""{header}
cat(sprintf("--- Day %d Problem %d ({disp}): %s ---\\n", {day}, {problem_num}, "{topic}"))
dataset <- c(10, 25, 30, 45, 60) * {day}
cat("Mean:", mean(dataset), "Sum:", sum(dataset), "\\n")
"""

    elif lang == "bash":
        code = f"""#!/usr/bin/env bash
{header}
echo "--- Day {day} Problem {problem_num} ({disp}): {topic} ---"
declare -a items=({day}0 {day}5 {day}8)
sum=0
for i in "${{items[@]}}"; do
  ((sum += i))
done
echo "Items: ${{items[*]}} | Sum: $sum"
"""

    elif lang == "sql":
        code = f"""{header}
-- Simulated Analytical Query for Day {day}
WITH DailyMetrics AS (
    SELECT 
        {day} AS DayNumber,
        {problem_num} AS ProblemIndex,
        '{disp}' AS ProgrammingLanguage,
        '{topic}' AS TopicCovered
)
SELECT * FROM DailyMetrics;
"""

    elif lang == "lua":
        code = f"""{header}
print(string.format("--- Day %d Problem %d ({disp}): %s ---", {day}, {problem_num}, "{topic}"))
local nums = {{{day} * 2, {day} * 4, {day} * 6}}
local sum = 0
for _, v in ipairs(nums) do sum = sum + v end
print("Sum of array elements:", sum)
"""

    elif lang == "julia":
        code = f"""{header}
println("--- Day {day} Problem {problem_num} ({disp}): {topic} ---")
arr = [1, 2, 3, 4, 5] .* {day}
println("Vector: ", arr, " | Sum: ", sum(arr))
"""

    elif lang == "haskell":
        code = f"""{header}
main :: IO ()
main = do
    putStrLn "--- Day {day} Problem {problem_num} ({disp}): {topic} ---"
    let nums = map (* {day}) [1..5]
    putStrLn ("List: " ++ show nums ++ " | Sum: " ++ show (sum nums))
"""

    elif lang == "elixir":
        code = f"""{header}
IO.puts("--- Day {day} Problem {problem_num} ({disp}): {topic} ---")
numbers = Enum.map(1..5, fn x -> x * {day} end)
IO.puts("Numbers: #{{inspect(numbers)}} | Sum: #{{Enum.sum(numbers)}}")
"""

    else:
        code = f"""{header}
// Day {day} Problem {problem_num} solution in {disp}
"""

    return filename, code

def generate_today():
    today_str = date.today().isoformat()
    state = load_state()

    current_day = state.get("current_day", 1)
    lang_index = state.get("lang_index", 0)

    # Pick language cycling through ALL available market languages
    lang = LANGUAGES[lang_index % len(LANGUAGES)]
    disp = LANGUAGE_CONFIG[lang]["display"]
    
    # Pick topic
    topic_tuple = TOPICS[(current_day - 1) % len(TOPICS)]
    topic_name = topic_tuple[0]

    lang_dir = os.path.join(WORKSPACE_DIR, lang)
    os.makedirs(lang_dir, exist_ok=True)

    created_files = []

    # 1. Problem 1
    f1_name, f1_code = generate_code_content(lang, current_day, 1, topic_name)
    f1_path = os.path.join(lang_dir, f1_name)
    with open(f1_path, "w") as f: f.write(f1_code)
    created_files.append((f1_name, f1_path))
    print(f"📄 Created: {lang}/{f1_name}")
    run_git(["add", os.path.relpath(f1_path, WORKSPACE_DIR)])
    run_git(["commit", "-m", f"feat({lang}): add day {current_day} problem 1 solution ({f1_name})"])

    # 2. Problem 2
    f2_name, f2_code = generate_code_content(lang, current_day, 2, topic_name)
    f2_path = os.path.join(lang_dir, f2_name)
    with open(f2_path, "w") as f: f.write(f2_code)
    created_files.append((f2_name, f2_path))
    print(f"📄 Created: {lang}/{f2_name}")
    run_git(["add", os.path.relpath(f2_path, WORKSPACE_DIR)])
    run_git(["commit", "-m", f"feat({lang}): add day {current_day} problem 2 solution ({f2_name})"])

    # 3. Update README & Tracker
    if os.path.exists(README_FILE):
        files_links = ", ".join([f"[`{fn}`]({lang}/{fn})" for fn, _ in created_files])
        table_entry = f"| **{today_str} (Day {current_day})** | `{disp}` | {topic_name} | {files_links} |\n"
        with open(README_FILE, "a") as f:
            f.write(table_entry)

        state["current_day"] = current_day + 1
        state["lang_index"] = lang_index + 1
        state["history"].append({
            "date": today_str,
            "day": current_day,
            "language": lang,
            "display": disp,
            "files": [f[0] for f in created_files]
        })
        save_state(state)

        run_git(["add", "README.md", "scripts/.daily_state.json"])
        run_git(["commit", "-m", f"docs: update daily learning log for Day {current_day} ({disp})"])

    print(f"\n✨ Successfully generated 2 {disp} problems with 3 separate daily commits for Day {current_day}!")

if __name__ == "__main__":
    generate_today()
