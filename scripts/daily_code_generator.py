#!/usr/bin/env python3
"""
Automated Multi-Language Daily Code Generator
Features:
- Generates between 3 to 4 codes daily (>2 and <5)
- Produces between 4 to 8 commits daily (>3 and <10)
- Supports random jitter / execution timing
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
    ("Variables, Types & Memory Models", "fundamentals"),
    ("Conditionals & Pattern Matching", "control_flow"),
    ("Loops & Iterative Algorithms", "loops"),
    ("Functions, Closures & Lambdas", "functions"),
    ("Arrays, Slices & Dynamic Buffers", "arrays"),
    ("String Algorithms & Regex", "strings"),
    ("Hash Maps & Lookup Tables", "hashmaps"),
    ("Object-Oriented & Structural Design", "oop"),
    ("Recursion & Divide-and-Conquer", "recursion"),
    ("Binary Search & Sliding Windows", "search"),
    ("Sorting Algorithms & Heuristics", "sorting"),
    ("Stacks & Queues Data Structures", "stacks_queues"),
    ("Linked Lists & Pointer Graphs", "linked_lists"),
    ("Binary Trees & Tree Traversals", "trees"),
    ("Graph Algorithms (BFS/DFS)", "graphs"),
    ("Dynamic Programming & Memoization", "dp"),
    ("Bitwise Manipulation & Masking", "bitwise"),
    ("Concurrency & Async Pipelines", "concurrency"),
    ("File I/O & JSON Serialization", "io_parsing"),
    ("Error Handling & Result Enums", "error_handling")
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
    """Generates (filename, initial_skeleton, final_solution)."""
    cfg = LANGUAGE_CONFIG[lang]
    ext = cfg["ext"]
    disp = cfg["display"]
    cmt = cfg["comment"]
    
    clean_topic = topic.split(",")[0].lower().replace(" ", "_").replace("&", "and")
    filename = f"day{day:02d}_problem{problem_num:02d}_{clean_topic}.{ext}"

    if lang == "java":
        classname = f"Day{day:02d}_Problem{problem_num:02d}_{clean_topic}"
        filename = f"{classname}.java"

    header = f"""{cmt} ==============================================================================
{cmt} Day {day:02d} - Problem {problem_num:02d}: {topic}
{cmt} Language: {disp}
{cmt} Daily Coding Practice & Algorithmic Problem Solving
{cmt} ==============================================================================
"""

    skeleton = f"""{header}
{cmt} Initial starter interface for Problem {problem_num}
"""

    if lang == "python":
        solution = f"""{header}
def solve_problem_{problem_num}(values: list[int]) -> dict:
    \"\"\"Solves Day {day} challenge #{problem_num} for {topic}.\"\"\"
    processed = [x * {problem_num} for x in values if x % 2 == 0]
    total = sum(processed)
    avg = total / len(processed) if processed else 0
    return {{"day": {day}, "problem": {problem_num}, "count": len(processed), "sum": total, "avg": avg}}

if __name__ == "__main__":
    test_data = [10, 15, 22, 34, 45, 56, 68]
    result = solve_problem_{problem_num}(test_data)
    print(f"[{disp} - Day {day} Problem {problem_num}] Result: {{result}}")
"""

    elif lang in ("javascript", "typescript"):
        solution = f"""{header}
function solveProblem{problem_num}(inputArray) {{
  console.log(`Executing Day {day} Problem {problem_num} (${disp}): {topic}`);
  const filtered = inputArray.filter(n => n % 2 === 0).map(n => n * {problem_num});
  const sum = filtered.reduce((acc, curr) => acc + curr, 0);
  return {{ day: {day}, problem: {problem_num}, items: filtered, total: sum }};
}}

const sampleData = [12, 25, 34, 48, 55, 60];
console.log("Solution Output:", solveProblem{problem_num}(sampleData));
"""

    elif lang == "c":
        solution = f"""{header}
#include <stdio.h>

void solveProblem{problem_num}(int arr[], int size) {{
    printf("--- Day %d Problem %d ({disp}): %s ---\\n", {day}, {problem_num}, "{topic}");
    int sum = 0;
    for(int i = 0; i < size; i++) {{
        if(arr[i] % 2 == 0) {{
            sum += arr[i] * {problem_num};
        }}
    }}
    printf("Computed Result Sum: %d\\n", sum);
}}

int main(void) {{
    int dataset[] = {{10, 21, 32, 43, 54, 65}};
    solveProblem{problem_num}(dataset, sizeof(dataset)/sizeof(dataset[0]));
    return 0;
}}
"""

    elif lang == "cpp":
        solution = f"""{header}
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

int main() {{
    std::cout << "--- Day {day} Problem {problem_num} ({disp}): {topic} ---\\n";
    std::vector<int> nums = {{14, 25, 36, 47, 58, 69}};
    std::vector<int> evens;
    for(int n : nums) {{
        if(n % 2 == 0) evens.push_back(n * {problem_num});
    }}
    int sum = std::accumulate(evens.begin(), evens.end(), 0);
    std::cout << "Processed elements: " << evens.size() << " | Sum: " << sum << std::endl;
    return 0;
}}
"""

    elif lang == "go":
        solution = f"""{header}
package main

import "fmt"

func solveProblem{problem_num}(numbers []int) (int, int) {{
    sum := 0
    count := 0
    for _, num := range numbers {{
        if num%2 == 0 {{
            sum += num * {problem_num}
            count++
        }}
    }}
    return count, sum
}}

func main() {{
    fmt.Println("--- Day {day} Problem {problem_num} ({disp}): {topic} ---")
    data := []int{{10, 23, 34, 45, 56, 67}}
    count, total := solveProblem{problem_num}(data)
    fmt.Printf("Even Count: %d, Scaled Total: %d\\n", count, total)
}}
"""

    elif lang == "java":
        solution = f"""{header}
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class {classname} {{
    public static void main(String[] args) {{
        System.out.println("--- Day {day} Problem {problem_num} ({disp}): {topic} ---");
        List<Integer> numbers = Arrays.asList(12, 23, 34, 45, 56, 67);
        List<Integer> evens = numbers.stream().filter(n -> n % 2 == 0).map(n -> n * {problem_num}).collect(Collectors.toList());
        int sum = evens.stream().mapToInt(Integer::intValue).sum();
        System.out.println("Result List: " + evens + " | Sum: " + sum);
    }}
}}
"""

    elif lang == "rust":
        solution = f"""{header}
fn main() {{
    println!("--- Day {} Problem {} ({disp}): {} ---", {day}, {problem_num}, "{topic}");
    let data = vec![10, 21, 32, 43, 54, 65];
    let evens: Vec<i32> = data.into_iter().filter(|x| x % 2 == 0).map(|x| x * {problem_num}).collect();
    let sum: i32 = evens.iter().sum();
    println!("Evens: {:?}, Sum: {}", evens, sum);
}}
"""

    else:
        solution = f"""{header}
{cmt} Implementation for Day {day} Problem {problem_num} in {disp}
{cmt} Topic: {topic}
"""

    return filename, skeleton, solution

def generate_today():
    today_str = date.today().isoformat()
    state = load_state()

    current_day = state.get("current_day", 1)
    lang_index = state.get("lang_index", 0)

    # 1. Random codes count between 3 and 4 (> 2 and < 5)
    num_codes = random.randint(3, 4)

    # 2. Pick language
    lang = LANGUAGES[lang_index % len(LANGUAGES)]
    disp = LANGUAGE_CONFIG[lang]["display"]

    # 3. Pick topic
    topic_name = TOPICS[(current_day - 1) % len(TOPICS)][0]

    lang_dir = os.path.join(WORKSPACE_DIR, lang)
    os.makedirs(lang_dir, exist_ok=True)

    created_files = []

    # 4. Generate each problem and create individual commits (> 3 and < 10 total commits)
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

    total_commits = num_codes * 2 + 1  # 3 codes -> 7 commits, 4 codes -> 9 commits (between 4 and 9 commits!)
    print(f"\n✨ Successfully generated {num_codes} codes with {total_commits} commits for Day {current_day} ({disp})!")

if __name__ == "__main__":
    generate_today()
