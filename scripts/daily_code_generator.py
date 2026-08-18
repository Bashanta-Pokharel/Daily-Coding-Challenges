#!/usr/bin/env python3
"""
Automated Daily Code Generator for Daily-Coding-Challenges
Generates 2 educational code files every day and creates 2-3 distinct commits:
- Commit 1: Solution 1
- Commit 2: Solution 2
- Commit 3: Updated Problem Log & Progress Tracker
"""

import os
import sys
import json
import subprocess
from datetime import datetime, date

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
STATE_FILE = os.path.join(WORKSPACE_DIR, "scripts", ".daily_state.json")
README_FILE = os.path.join(WORKSPACE_DIR, "README.md")

LANGUAGES = ["python", "javascript", "c", "cpp", "java", "go"]

CURRICULUM = [
    # Day 1
    {
        "day": 1,
        "topic": "Variables & Core Data Types",
        "codes": {
            "python": [
                ("day01_01_hello_variables.py", '"""\nDay 1 - Problem 1: Basic Variables & Types in Python\n"""\nname = "Developer"\nage = 25\nheight = 5.9\nis_learning = True\nprint(f"Name: {name}, Age: {age}, Height: {height}, Learning: {is_learning}")\n'),
                ("day01_02_basic_calculator.py", '"""\nDay 1 - Problem 2: Basic Arithmetic Calculator in Python\n"""\ndef calculate(a: float, b: float, op: str):\n    if op == "+": return a + b\n    elif op == "-": return a - b\n    elif op == "*": return a * b\n    elif op == "/": return a / b if b != 0 else "Error: Div by 0"\n    return "Invalid operator"\nprint("10 + 5 =", calculate(10, 5, "+"))\nprint("20 / 4 =", calculate(20, 4, "/"))\n')
            ]
        }
    },
    # Day 2
    {
        "day": 2,
        "topic": "Control Flow & Loops",
        "codes": {
            "javascript": [
                ("day02_01_fizzbuzz.js", '// Day 2 - Problem 1: Classic FizzBuzz\nfor (let i = 1; i <= 25; i++) {\n  let out = "";\n  if (i % 3 === 0) out += "Fizz";\n  if (i % 5 === 0) out += "Buzz";\n  console.log(out || i);\n}\n'),
                ("day02_02_array_filter.js", '// Day 2 - Problem 2: Array Filtering & Mapping\nconst nums = [12, 45, 68, 23, 89, 90, 34];\nconst evensDoubled = nums.filter(n => n % 2 === 0).map(n => n * 2);\nconsole.log("Evens Doubled:", evensDoubled);\n')
            ]
        }
    },
    # Day 3
    {
        "day": 3,
        "topic": "Pointers & Memory Allocation",
        "codes": {
            "c": [
                ("day03_01_reverse_number.c", '#include <stdio.h>\nlong reverse(long n) {\n    long r = 0;\n    while(n) { r = r*10 + (n%10); n/=10; }\n    return r;\n}\nint main(void) {\n    printf("Reversed: %ld\\n", reverse(987654321));\n    return 0;\n}\n'),
                ("day03_02_factorial.c", '#include <stdio.h>\nunsigned long long fact(int n) {\n    unsigned long long res = 1;\n    for(int i=2; i<=n; i++) res *= i;\n    return res;\n}\nint main(void) {\n    printf("10! = %llu\\n", fact(10));\n    return 0;\n}\n')
            ]
        }
    },
    # Day 4
    {
        "day": 4,
        "topic": "STL Algorithms & Vectors",
        "codes": {
            "cpp": [
                ("day04_01_binary_search.cpp", '#include <iostream>\n#include <vector>\nint binarySearch(const std::vector<int>& v, int t) {\n    int l = 0, r = v.size() - 1;\n    while(l <= r) {\n        int m = l + (r - l)/2;\n        if(v[m] == t) return m;\n        if(v[m] < t) l = m + 1; else r = m - 1;\n    }\n    return -1;\n}\nint main() {\n    std::vector<int> arr = {1, 3, 5, 7, 9, 11};\n    std::cout << "Index of 7: " << binarySearch(arr, 7) << std::endl;\n    return 0;\n}\n'),
                ("day04_02_vector_minmax.cpp", '#include <iostream>\n#include <vector>\n#include <algorithm>\nint main() {\n    std::vector<int> v = {45, 12, 89, 34, 67};\n    std::cout << "Min: " << *std::min_element(v.begin(), v.end()) << "\\n";\n    std::cout << "Max: " << *std::max_element(v.begin(), v.end()) << "\\n";\n    return 0;\n}\n')
            ]
        }
    },
    # Day 5
    {
        "day": 5,
        "topic": "Collections & HashMaps",
        "codes": {
            "java": [
                ("day05_01_AnagramChecker.java", 'import java.util.Arrays;\npublic class day05_01_AnagramChecker {\n    public static boolean isAnagram(String s1, String s2) {\n        char[] a = s1.toLowerCase().toCharArray();\n        char[] b = s2.toLowerCase().toCharArray();\n        Arrays.sort(a); Arrays.sort(b);\n        return Arrays.equals(a, b);\n    }\n    public static void main(String[] args) {\n        System.out.println("listen & silent: " + isAnagram("listen", "silent"));\n    }\n}\n'),
                ("day05_02_SecondLargest.java", 'public class day05_02_SecondLargest {\n    public static void main(String[] args) {\n        int[] arr = {10, 45, 23, 89, 67};\n        int m1 = -1, m2 = -1;\n        for(int n : arr) {\n            if(n > m1) { m2 = m1; m1 = n; }\n            else if(n > m2 && n != m1) m2 = n;\n        }\n        System.out.println("Second largest: " + m2);\n    }\n}\n')
            ]
        }
    },
    # Day 6
    {
        "day": 6,
        "topic": "Slices & Concurrency",
        "codes": {
            "go": [
                ("day06_01_slice_rotator.go", 'package main\nimport "fmt"\nfunc rotate(nums []int, k int) []int {\n    k = k % len(nums)\n    return append(nums[len(nums)-k:], nums[:len(nums)-k]...)\n}\nfunc main() {\n    fmt.Println(rotate([]int{1,2,3,4,5}, 2))\n}\n'),
                ("day06_02_word_count.go", 'package main\nimport ("fmt"; "strings")\nfunc main() {\n    text := "go is fast and go is clean"\n    counts := make(map[string]int)\n    for _, w := range strings.Fields(text) { counts[w]++ }\n    fmt.Println(counts)\n}\n')
            ]
        }
    }
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
        print(f"Git command failed: {e}")

def generate_today():
    today_str = date.today().isoformat()
    state = load_state()

    current_day = state.get("current_day", 1)
    lang_index = state.get("lang_index", 0)

    # Pick rotating language
    lang = LANGUAGES[lang_index % len(LANGUAGES)]
    
    curr_item = next((c for c in CURRICULUM if c["day"] == current_day), None)
    if not curr_item:
        curr_item = CURRICULUM[(current_day - 1) % len(CURRICULUM)]

    codes = curr_item["codes"].get(lang, [])
    if not codes:
        # Fallback to any language available in item
        codes = next(iter(curr_item["codes"].values()))

    lang_dir = os.path.join(WORKSPACE_DIR, lang)
    os.makedirs(lang_dir, exist_ok=True)

    created_files = []
    
    # 1. Create Problem 1 & Make Commit 1
    if len(codes) > 0:
        f1_name, f1_code = codes[0]
        f1_path = os.path.join(lang_dir, f1_name)
        with open(f1_path, "w") as f: f.write(f1_code)
        created_files.append((f1_name, f1_path))
        print(f"📄 Created: {lang}/{f1_name}")
        run_git(["add", os.path.relpath(f1_path, WORKSPACE_DIR)])
        run_git(["commit", "-m", f"feat({lang}): add day {current_day} solution - {f1_name}"])

    # 2. Create Problem 2 & Make Commit 2
    if len(codes) > 1:
        f2_name, f2_code = codes[1]
        f2_path = os.path.join(lang_dir, f2_name)
        with open(f2_path, "w") as f: f.write(f2_code)
        created_files.append((f2_name, f2_path))
        print(f"📄 Created: {lang}/{f2_name}")
        run_git(["add", os.path.relpath(f2_path, WORKSPACE_DIR)])
        run_git(["commit", "-m", f"feat({lang}): add day {current_day} solution - {f2_name}"])

    # 3. Update Progress Log & Make Commit 3
    if os.path.exists(README_FILE):
        files_links = ", ".join([f"[`{fn}`]({lang}/{fn})" for fn, _ in created_files])
        table_entry = f"| **{today_str} (Day {current_day})** | `{lang.upper()}` | {curr_item['topic']} | {files_links} |\n"
        with open(README_FILE, "a") as f:
            f.write(table_entry)
        
        # Save state
        state["current_day"] = current_day + 1
        state["lang_index"] = lang_index + 1
        state["history"].append({
            "date": today_str,
            "day": current_day,
            "language": lang,
            "files": [f[0] for f in created_files]
        })
        save_state(state)

        run_git(["add", "README.md", "scripts/.daily_state.json"])
        run_git(["commit", "-m", f"docs: update daily challenge log & curriculum tracker (Day {current_day})"])

    print(f"\n✨ Generated 2 {lang.upper()} exercises with 3 separate daily commits for Day {current_day}!")

if __name__ == "__main__":
    generate_today()
