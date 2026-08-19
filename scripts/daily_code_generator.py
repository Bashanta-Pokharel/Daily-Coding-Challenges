#!/usr/bin/env python3
"""
Automated Multi-Language Daily Code Generator
Features:
- Generates between 3 to 4 codes daily (>2 and <5)
- Produces between 4 to 9 commits daily (>3 and <10)
- Executes randomly between 11:00 PM and 11:59 PM
- Rotates across all 22 major market programming languages
"""

import os
import sys
import json
import random
import time
import subprocess
from datetime import datetime, date

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
STATE_FILE = os.path.join(WORKSPACE_DIR, "scripts", ".daily_state.json")
README_FILE = os.path.join(WORKSPACE_DIR, "README.md")

LANGUAGE_CONFIG = {
    "python": {"ext": "py", "comment": "#", "display": "Python"},
    "javascript": {"ext": "js", "comment": "//", "display": "JavaScript"},
    "typescript": {"ext": "ts", "comment": "//", "display": "TypeScript"},
    "c": {"ext": "c", "comment": "//", "display": "C"},
    "cpp": {"ext": "cpp", "comment": "//", "display": "C++"},
    "csharp": {"ext": "cs", "comment": "//", "display": "C#"},
    "java": {"ext": "java", "comment": "//", "display": "Java"},
    "kotlin": {"ext": "kt", "comment": "//", "display": "Kotlin"},
    "swift": {"ext": "swift", "comment": "//", "display": "Swift"},
    "go": {"ext": "go", "comment": "//", "display": "Go"},
    "rust": {"ext": "rs", "comment": "//", "display": "Rust"},
    "php": {"ext": "php", "comment": "//", "display": "PHP"},
    "ruby": {"ext": "rb", "comment": "#", "display": "Ruby"},
    "dart": {"ext": "dart", "comment": "//", "display": "Dart"},
    "scala": {"ext": "scala", "comment": "//", "display": "Scala"},
    "r": {"ext": "r", "comment": "#", "display": "R"},
    "bash": {"ext": "sh", "comment": "#", "display": "Bash"},
    "sql": {"ext": "sql", "comment": "--", "display": "SQL"},
    "lua": {"ext": "lua", "comment": "--", "display": "Lua"},
    "julia": {"ext": "jl", "comment": "#", "display": "Julia"},
    "haskell": {"ext": "hs", "comment": "--", "display": "Haskell"},
    "elixir": {"ext": "ex", "comment": "#", "display": "Elixir"}
}

LANGUAGES = list(LANGUAGE_CONFIG.keys())

TOPICS = [
    ("Variables, Types and Memory Models", "fundamentals"),
    ("Conditionals and Pattern Matching", "control_flow"),
    ("Loops and Iterative Algorithms", "loops"),
    ("Functions, Closures and Lambdas", "functions"),
    ("Arrays, Slices and Dynamic Buffers", "arrays"),
    ("String Algorithms and Parsing", "strings"),
    ("Hash Maps and Lookup Tables", "hashmaps"),
    ("Object-Oriented and Structural Design", "oop"),
    ("Recursion and Divide-and-Conquer", "recursion"),
    ("Binary Search and Sliding Windows", "search"),
    ("Sorting Algorithms and Heuristics", "sorting"),
    ("Stacks and Queues Data Structures", "stacks_queues"),
    ("Linked Lists and Pointer Graphs", "linked_lists"),
    ("Binary Trees and Tree Traversals", "trees"),
    ("Graph Algorithms BFS and DFS", "graphs"),
    ("Dynamic Programming and Memoization", "dp"),
    ("Bitwise Manipulation and Masking", "bitwise"),
    ("Concurrency and Async Pipelines", "concurrency"),
    ("File IO and Data Serialization", "io_parsing"),
    ("Error Handling and Result Enums", "error_handling")
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

def generate_code_content(lang: str, day: int, problem_num: int, topic: str) -> tuple[str, str, str]:
    cfg = LANGUAGE_CONFIG[lang]
    ext = cfg["ext"]
    disp = cfg["display"]
    cmt = cfg["comment"]
    
    clean_topic = topic.split(",")[0].lower().replace(" ", "_").replace("&", "and")
    filename = f"day{day:02d}_problem{problem_num:02d}_{clean_topic}.{ext}"

    if lang == "java":
        classname = f"Day{day:02d}_Problem{problem_num:02d}_{clean_topic}"
        filename = f"{classname}.java"

    header = (
        f"{cmt} ==============================================================================\n"
        f"{cmt} Day {day:02d} - Problem {problem_num:02d}: {topic}\n"
        f"{cmt} Language: {disp}\n"
        f"{cmt} Daily Coding Practice & Algorithmic Problem Solving\n"
        f"{cmt} ==============================================================================\n"
    )

    skeleton = (
        f"{header}\n"
        f"{cmt} Initial starter interface for Problem {problem_num}\n"
    )

    if lang == "python":
        solution = (
            f"{header}\n"
            f"def solve_problem_{problem_num}(values: list[int]) -> dict:\n"
            f'    """Solves Day {day} challenge #{problem_num} for {topic}."""\n'
            f"    processed = [x * {problem_num} for x in values if x % 2 == 0]\n"
            f"    total = sum(processed)\n"
            f"    avg = total / len(processed) if processed else 0\n"
            f'    return {{"day": {day}, "problem": {problem_num}, "count": len(processed), "sum": total, "avg": avg}}\n\n'
            f'if __name__ == "__main__":\n'
            f"    test_data = [10, 15, 22, 34, 45, 56, 68]\n"
            f"    result = solve_problem_{problem_num}(test_data)\n"
            f'    print(f"[{disp} - Day {day} Problem {problem_num}] Result: {{result}}")\n'
        )

    elif lang in ("javascript", "typescript"):
        solution = (
            f"{header}\n"
            f"function solveProblem{problem_num}(inputArray) {{\n"
            f"  console.log(`Executing Day {day} Problem {problem_num} (${disp}): {topic}`);\n"
            f"  const filtered = inputArray.filter(n => n % 2 === 0).map(n => n * {problem_num});\n"
            f"  const sum = filtered.reduce((acc, curr) => acc + curr, 0);\n"
            f"  return {{ day: {day}, problem: {problem_num}, items: filtered, total: sum }};\n"
            f"}}\n\n"
            f"const sampleData = [12, 25, 34, 48, 55, 60];\n"
            f'console.log("Solution Output:", solveProblem{problem_num}(sampleData));\n'
        )

    elif lang == "c":
        solution = (
            f"{header}\n"
            f"#include <stdio.h>\n\n"
            f"void solveProblem{problem_num}(int arr[], int size) {{\n"
            f'    printf("--- Day %d Problem %d ({disp}): %s ---\\n", {day}, {problem_num}, "{topic}");\n'
            f"    int sum = 0;\n"
            f"    for(int i = 0; i < size; i++) {{\n"
            f"        if(arr[i] % 2 == 0) {{\n"
            f"            sum += arr[i] * {problem_num};\n"
            f"        }}\n"
            f"    }}\n"
            f'    printf("Computed Result Sum: %d\\n", sum);\n'
            f"}}\n\n"
            f"int main(void) {{\n"
            f"    int dataset[] = {{10, 21, 32, 43, 54, 65}};\n"
            f"    solveProblem{problem_num}(dataset, sizeof(dataset)/sizeof(dataset[0]));\n"
            f"    return 0;\n"
            f"}}\n"
        )

    elif lang == "cpp":
        solution = (
            f"{header}\n"
            f"#include <iostream>\n"
            f"#include <vector>\n"
            f"#include <numeric>\n"
            f"#include <algorithm>\n\n"
            f"int main() {{\n"
            f'    std::cout << "--- Day {day} Problem {problem_num} ({disp}): {topic} ---\\n";\n'
            f"    std::vector<int> nums = {{14, 25, 36, 47, 58, 69}};\n"
            f"    std::vector<int> evens;\n"
            f"    for(int n : nums) {{\n"
            f"        if(n % 2 == 0) evens.push_back(n * {problem_num});\n"
            f"    }}\n"
            f"    int sum = std::accumulate(evens.begin(), evens.end(), 0);\n"
            f'    std::cout << "Processed elements: " << evens.size() << " | Sum: " << sum << std::endl;\n'
            f"    return 0;\n"
            f"}}\n"
        )

    elif lang == "go":
        solution = (
            f"{header}\n"
            f"package main\n\n"
            f'import "fmt"\n\n'
            f"func solveProblem{problem_num}(numbers []int) (int, int) {{\n"
            f"    sum := 0\n"
            f"    count := 0\n"
            f"    for _, num := range numbers {{\n"
            f"        if num%2 == 0 {{\n"
            f"            sum += num * {problem_num}\n"
            f"            count++\n"
            f"        }}\n"
            f"    }}\n"
            f"    return count, sum\n"
            f"}}\n\n"
            f"func main() {{\n"
            f'    fmt.Println("--- Day {day} Problem {problem_num} ({disp}): {topic} ---")\n'
            f"    data := []int{{10, 23, 34, 45, 56, 67}}\n"
            f"    count, total := solveProblem{problem_num}(data)\n"
            f'    fmt.Printf("Even Count: %d, Scaled Total: %d\\n", count, total)\n'
            f"}}\n"
        )

    elif lang == "java":
        solution = (
            f"{header}\n"
            f"import java.util.Arrays;\n"
            f"import java.util.List;\n"
            f"import java.util.stream.Collectors;\n\n"
            f"public class {classname} {{\n"
            f"    public static void main(String[] args) {{\n"
            f'        System.out.println("--- Day {day} Problem {problem_num} ({disp}): {topic} ---");\n'
            f"        List<Integer> numbers = Arrays.asList(12, 23, 34, 45, 56, 67);\n"
            f"        List<Integer> evens = numbers.stream().filter(n -> n % 2 == 0).map(n -> n * {problem_num}).collect(Collectors.toList());\n"
            f"        int sum = evens.stream().mapToInt(Integer::intValue).sum();\n"
            f'        System.out.println("Result List: " + evens + " | Sum: " + sum);\n'
            f"    }}\n"
            f"}}\n"
        )

    elif lang == "rust":
        solution = (
            f"{header}\n"
            f"fn main() {{\n"
            f'    println!("--- Day {{}} Problem {{}} ({disp}): {{}} ---", {day}, {problem_num}, "{topic}");\n'
            f"    let data = vec![10, 21, 32, 43, 54, 65];\n"
            f"    let evens: Vec<i32> = data.into_iter().filter(|x| x % 2 == 0).map(|x| x * {problem_num}).collect();\n"
            f"    let sum: i32 = evens.iter().sum();\n"
            f'    println!("Evens: {{:?}}, Sum: {{}}", evens, sum);\n'
            f"}}\n"
        )

    else:
        solution = (
            f"{header}\n"
            f"{cmt} Implementation for Day {day} Problem {problem_num} in {disp}\n"
            f"{cmt} Topic: {topic}\n"
        )

    return filename, skeleton, solution

def generate_today():
    today_str = date.today().isoformat()
    state = load_state()

    current_day = state.get("current_day", 1)
    lang_index = state.get("lang_index", 0)

    # Random codes count between 3 and 4 (> 2 and < 5)
    num_codes = random.randint(3, 4)

    # Pick language
    lang = LANGUAGES[lang_index % len(LANGUAGES)]
    disp = LANGUAGE_CONFIG[lang]["display"]

    # Pick topic
    topic_name = TOPICS[(current_day - 1) % len(TOPICS)][0]

    lang_dir = os.path.join(WORKSPACE_DIR, lang)
    os.makedirs(lang_dir, exist_ok=True)

    created_files = []

    # Generate each problem and create individual commits (> 3 and < 10 total commits)
    for p_num in range(1, num_codes + 1):
        fname, skeleton, solution = generate_code_content(lang, current_day, p_num, topic_name)
        fpath = os.path.join(lang_dir, fname)

        # Step A: Initial skeleton commit
        with open(fpath, "w") as f:
            f.write(skeleton)
        run_git(["add", os.path.relpath(fpath, WORKSPACE_DIR)])
        run_git(["commit", "-m", f"feat({lang}): add initial structure for day {current_day} problem {p_num}"])

        # Step B: Full solution implementation commit
        with open(fpath, "w") as f:
            f.write(solution)
        run_git(["add", os.path.relpath(fpath, WORKSPACE_DIR)])
        run_git(["commit", "-m", f"feat({lang}): implement day {current_day} problem {p_num} solution - {topic_name}"])

        created_files.append((fname, fpath))
        print(f"📄 Generated & Committed ({p_num}/{num_codes}): {lang}/{fname}")

    # Step C: Update README problem log and create final tracking commit
    if os.path.exists(README_FILE):
        files_links = ", ".join([f"[`{fn}`]({lang}/{fn})" for fn, _ in created_files])
        table_entry = f"| **{today_str} (Day {current_day})** | `{disp}` | {topic_name} ({num_codes} problems) | {files_links} |\n"
        with open(README_FILE, "a") as f:
            f.write(table_entry)

        state["current_day"] = current_day + 1
        state["lang_index"] = lang_index + 1
        state["history"].append({
            "date": today_str,
            "day": current_day,
            "language": lang,
            "problems_count": num_codes,
            "files": [f[0] for f in created_files]
        })
        save_state(state)

        run_git(["add", "README.md", "scripts/.daily_state.json"])
        run_git(["commit", "-m", f"docs: update daily practice log for Day {current_day} ({disp} - {num_codes} problems)"])

    total_commits = num_codes * 2 + 1
    print(f"\n✨ Successfully generated {num_codes} codes with {total_commits} commits for Day {current_day} ({disp})!")

if __name__ == "__main__":
    generate_today()
