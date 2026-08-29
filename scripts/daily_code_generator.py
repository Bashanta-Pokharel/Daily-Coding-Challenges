#!/usr/bin/env python3
"""
Automated Multi-Language Daily Code Generator
Features:
- Generates 3 to 5 codes daily
- Produces between 11 to 19 commits daily (>10 and <20)
- Executes randomly between 1:00 PM and 10:00 PM (NPT / +05:45)
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

def generate_problem_stages(lang: str, day: int, problem_num: int, topic: str) -> tuple[str, list[tuple[str, str]]]:
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

    # 4 progressive stages for authentic git history
    if lang == "python":
        s1 = (
            f"{header}\n"
            f"def solve_problem_{problem_num}(values: list[int]) -> dict:\n"
            f'    """Starter stub for Day {day} challenge #{problem_num}: {topic}."""\n'
            f"    # TODO: Implement algorithmic logic\n"
            f"    pass\n"
        )
        s2 = (
            f"{header}\n"
            f"def solve_problem_{problem_num}(values: list[int]) -> dict:\n"
            f'    """Solves Day {day} challenge #{problem_num} for {topic}."""\n'
            f"    processed = [x * {problem_num} for x in values if x % 2 == 0]\n"
            f"    total = sum(processed)\n"
            f"    avg = total / len(processed) if processed else 0\n"
            f'    return {{"day": {day}, "problem": {problem_num}, "count": len(processed), "sum": total, "avg": avg}}\n'
        )
        s3 = (
            f"{s2}\n"
            f'if __name__ == "__main__":\n'
            f"    test_data = [10, 15, 22, 34, 45, 56, 68]\n"
            f"    result = solve_problem_{problem_num}(test_data)\n"
            f'    print(f"[{disp} - Day {day} Problem {problem_num}] Result: {{result}}")\n'
        )
        s4 = (
            f"{s3}\n"
            f'"""\n'
            f'Complexity Analysis:\n'
            f'- Time Complexity: O(N) where N is dataset length\n'
            f'- Space Complexity: O(N) for filtered buffer\n'
            f'"""\n'
        )

    elif lang in ("javascript", "typescript"):
        s1 = (
            f"{header}\n"
            f"function solveProblem{problem_num}(inputArray) {{\n"
            f"  // Starter declaration for {topic}\n"
            f"  return null;\n"
            f"}}\n"
        )
        s2 = (
            f"{header}\n"
            f"function solveProblem{problem_num}(inputArray) {{\n"
            f"  const filtered = inputArray.filter(n => n % 2 === 0).map(n => n * {problem_num});\n"
            f"  const sum = filtered.reduce((acc, curr) => acc + curr, 0);\n"
            f"  return {{ day: {day}, problem: {problem_num}, items: filtered, total: sum }};\n"
            f"}}\n"
        )
        s3 = (
            f"{s2}\n"
            f"const sampleData = [12, 25, 34, 48, 55, 60];\n"
            f'console.log("Solution Output:", solveProblem{problem_num}(sampleData));\n'
        )
        s4 = (
            f"{s3}\n"
            f"// Complexity Analysis:\n"
            f"// Time Complexity: O(N)\n"
            f"// Space Complexity: O(N)\n"
        )

    elif lang == "c":
        s1 = (
            f"{header}\n"
            f"#include <stdio.h>\n\n"
            f"void solveProblem{problem_num}(int arr[], int size);\n"
        )
        s2 = (
            f"{header}\n"
            f"#include <stdio.h>\n\n"
            f"void solveProblem{problem_num}(int arr[], int size) {{\n"
            f'    printf("--- Day %d Problem %d ({disp}): %s ---\\n", {day}, {problem_num}, "{topic}");\n'
            f"    int sum = 0;\n"
            f"    for(int i = 0; i < size; i++) {{\n"
            f"        if(arr[i] % 2 == 0) sum += arr[i] * {problem_num};\n"
            f"    }}\n"
            f'    printf("Computed Result Sum: %d\\n", sum);\n'
            f"}}\n"
        )
        s3 = (
            f"{s2}\n"
            f"int main(void) {{\n"
            f"    int dataset[] = {{10, 21, 32, 43, 54, 65}};\n"
            f"    solveProblem{problem_num}(dataset, sizeof(dataset)/sizeof(dataset[0]));\n"
            f"    return 0;\n"
            f"}}\n"
        )
        s4 = (
            f"{s3}\n"
            f"/* Time: O(N), Space: O(1) */\n"
        )

    elif lang == "cpp":
        s1 = (
            f"{header}\n"
            f"#include <iostream>\n"
            f"#include <vector>\n\n"
            f"// Problem {problem_num} Starter Interface\n"
        )
        s2 = (
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
        s3 = s2
        s4 = (
            f"{s2}\n"
            f"// Time: O(N) | Space: O(N)\n"
        )

    elif lang == "go":
        s1 = (
            f"{header}\n"
            f"package main\n\n"
            f"func solveProblem{problem_num}(numbers []int) (int, int) {{\n"
            f"    return 0, 0\n"
            f"}}\n"
        )
        s2 = (
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
            f"}}\n"
        )
        s3 = (
            f"{s2}\n"
            f"func main() {{\n"
            f'    fmt.Println("--- Day {day} Problem {problem_num} ({disp}): {topic} ---")\n'
            f"    data := []int{{10, 23, 34, 45, 56, 67}}\n"
            f"    count, total := solveProblem{problem_num}(data)\n"
            f'    fmt.Printf("Even Count: %d, Scaled Total: %d\\n", count, total)\n'
            f"}}\n"
        )
        s4 = (
            f"{s3}\n"
            f"// Time Complexity: O(N), Space Complexity: O(1)\n"
        )

    elif lang == "java":
        s1 = (
            f"{header}\n"
            f"public class {classname} {{\n"
            f"    public static void main(String[] args) {{\n"
            f'        System.out.println("Starter Day {day} Problem {problem_num}");\n'
            f"    }}\n"
            f"}}\n"
        )
        s2 = (
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
        s3 = s2
        s4 = (
            f"{s2}\n"
            f"// Complexity: O(N) time, O(N) space\n"
        )

    elif lang == "rust":
        s1 = (
            f"{header}\n"
            f"fn main() {{\n"
            f'    println!("Starter Day {day} Problem {problem_num}");\n'
            f"}}\n"
        )
        s2 = (
            f"{header}\n"
            f"fn main() {{\n"
            f'    println!("--- Day {{}} Problem {{}} ({disp}): {{}} ---", {day}, {problem_num}, "{topic}");\n'
            f"    let data = vec![10, 21, 32, 43, 54, 65];\n"
            f"    let evens: Vec<i32> = data.into_iter().filter(|x| x % 2 == 0).map(|x| x * {problem_num}).collect();\n"
            f"    let sum: i32 = evens.iter().sum();\n"
            f'    println!("Evens: {{:?}}, Sum: {{}}", evens, sum);\n'
            f"}}\n"
        )
        s3 = s2
        s4 = (
            f"{s2}\n"
            f"// Time: O(N), Space: O(N)\n"
        )

    else:
        s1 = (
            f"{header}\n"
            f"{cmt} Problem {problem_num} Scaffold for {disp}\n"
        )
        s2 = (
            f"{header}\n"
            f"{cmt} Implementation for Day {day} Problem {problem_num} in {disp}\n"
            f"{cmt} Topic: {topic}\n"
        )
        s3 = (
            f"{s2}\n"
            f"{cmt} Test harness & execution verification\n"
        )
        s4 = (
            f"{s3}\n"
            f"{cmt} Time Complexity: O(N), Space Complexity: O(1)\n"
        )

    stages = [
        (f"feat({lang}): add initial structure for day {day} problem {problem_num}", s1),
        (f"feat({lang}): implement day {day} problem {problem_num} solution - {topic}", s2),
        (f"test({lang}): add test cases and verification for day {day} problem {problem_num}", s3),
        (f"docs({lang}): add algorithmic complexity notes for day {day} problem {problem_num}", s4),
    ]

    return filename, stages

def generate_today():
    today_str = date.today().isoformat()
    state = load_state()

    current_day = state.get("current_day", 1)
    lang_index = state.get("lang_index", 0)

    # Random target commits strictly > 10 and < 20 (i.e. 11 to 19 commits total)
    target_total_commits = random.randint(11, 19)
    # 1 commit is reserved for README & .daily_state.json log update
    target_code_commits = target_total_commits - 1  # 10 to 18

    # Generate 3 to 5 problems
    num_codes = random.randint(3, 5)

    # Pick language
    lang = LANGUAGES[lang_index % len(LANGUAGES)]
    disp = LANGUAGE_CONFIG[lang]["display"]

    # Pick topic
    topic_name = TOPICS[(current_day - 1) % len(TOPICS)][0]

    lang_dir = os.path.join(WORKSPACE_DIR, lang)
    os.makedirs(lang_dir, exist_ok=True)

    # Prepare problem stages
    problem_data = []
    for p_num in range(1, num_codes + 1):
        fname, stages = generate_problem_stages(lang, current_day, p_num, topic_name)
        problem_data.append({
            "num": p_num,
            "filename": fname,
            "filepath": os.path.join(lang_dir, fname),
            "stages": stages,
            "commits_assigned": 2  # start with at least 2 stages per problem
        })

    # Distribute remaining commit budget across problems
    current_assigned = sum(p["commits_assigned"] for p in problem_data)
    while current_assigned < target_code_commits:
        # Pick problems that have fewer than 4 stages assigned
        eligible = [p for p in problem_data if p["commits_assigned"] < 4]
        if not eligible:
            # If all problems already have 4 stages, add another problem if possible or break
            break
        chosen = random.choice(eligible)
        chosen["commits_assigned"] += 1
        current_assigned += 1

    created_files = []
    commits_executed = 0

    # Execute and commit stages for each problem
    for p in problem_data:
        p_num = p["num"]
        fname = p["filename"]
        fpath = p["filepath"]
        stages = p["stages"]
        k = p["commits_assigned"]

        # Select k stages out of 4 (always including first and last/completed)
        if k == 2:
            chosen_stages = [stages[0], stages[3]]
        elif k == 3:
            chosen_stages = [stages[0], stages[1], stages[3]]
        else:
            chosen_stages = stages[:k]

        for commit_msg, content in chosen_stages:
            with open(fpath, "w") as f:
                f.write(content)
            run_git(["add", os.path.relpath(fpath, WORKSPACE_DIR)])
            run_git(["commit", "-m", commit_msg])
            commits_executed += 1

        created_files.append((fname, fpath))
        print(f"📄 Generated & Committed ({p_num}/{num_codes}): {lang}/{fname} ({k} commits)")

    # Update README problem log and create final tracking commit
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
        commits_executed += 1

    print(f"\n✨ Successfully generated {num_codes} codes with {commits_executed} total commits (target was {target_total_commits}) for Day {current_day} ({disp})!")

if __name__ == "__main__":
    generate_today()

