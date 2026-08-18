#!/usr/bin/env python3
"""
Automated Daily Code Generator for Daily-Coding-Challenges
Generates 2 educational code files every day across rotating programming languages
(Python, JavaScript, C, C++, Java, Go), tracks progress in README.md,
and commits changes automatically.
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
    # Day 1: Hello World & Variables
    {
        "day": 1,
        "topic": "Fundamentals: Variables & Data Types",
        "codes": {
            "python": [
                ("day01_01_hello_variables.py", '"""\nDay 1 - Problem 1: Basic Variables & Types in Python\n"""\n\nname = "Developer"\nage = 25\nheight = 5.9\nis_learning = True\n\nprint(f"Name: {name} ({type(name).__name__})")\nprint(f"Age: {age} ({type(age).__name__})")\nprint(f"Height: {height} ({type(height).__name__})")\nprint(f"Learning: {is_learning} ({type(is_learning).__name__})")\n'),
                ("day01_02_basic_calculator.py", '"""\nDay 1 - Problem 2: Basic Arithmetic Calculator in Python\n"""\n\ndef calculate(a: float, b: float, op: str):\n    if op == "+": return a + b\n    elif op == "-": return a - b\n    elif op == "*": return a * b\n    elif op == "/": return a / b if b != 0 else "Error: Div by 0"\n    return "Invalid operator"\n\nprint("10 + 5 =", calculate(10, 5, "+"))\nprint("20 / 4 =", calculate(20, 4, "/"))\n')
            ],
            "javascript": [
                ("day01_01_basics_and_data_types.js", '// Day 1 - Problem 1: JS Basics & Primitive Types\nconst lang = "JavaScript";\nlet version = 2026;\nlet isAwesome = true;\n\nconsole.log(`Language: ${lang}, Year: ${version}, Active: ${isAwesome}`);\n'),
                ("day01_02_palindrome_checker.js", '// Day 1 - Problem 2: Palindrome Checker\nfunction isPalindrome(str) {\n  const clean = str.toLowerCase().replace(/[^a-z0-9]/g, "");\n  return clean === clean.split("").reverse().join("");\n}\n\nconsole.log("racecar ->", isPalindrome("racecar"));\nconsole.log("hello ->", isPalindrome("hello"));\n')
            ],
            "c": [
                ("day01_01_hello_variables.c", '#include <stdio.h>\n\nint main(void) {\n    int age = 25;\n    float score = 94.5f;\n    char grade = \'A\';\n    printf("Age: %d, Score: %.1f, Grade: %c\\n", age, score, grade);\n    return 0;\n}\n'),
                ("day01_02_even_odd_checker.c", '#include <stdio.h>\n#include <stdbool.h>\n\nbool isEven(int n) {\n    return (n % 2) == 0;\n}\n\nint main(void) {\n    int nums[] = {2, 7, 14, 21, 30};\n    for(int i=0; i<5; i++) {\n        printf("%d is %s\\n", nums[i], isEven(nums[i]) ? "Even" : "Odd");\n    }\n    return 0;\n}\n')
            ],
            "cpp": [
                ("day01_01_basic_io_and_types.cpp", '#include <iostream>\n#include <string>\n\nint main() {\n    std::string topic = "Modern C++ Basics";\n    int day = 1;\n    std::cout << topic << " - Day " << day << std::endl;\n    return 0;\n}\n'),
                ("day01_02_array_sum_and_average.cpp", '#include <iostream>\n#include <vector>\n#include <numeric>\n\nint main() {\n    std::vector<int> nums = {10, 20, 30, 40, 50};\n    int sum = std::accumulate(nums.begin(), nums.end(), 0);\n    double avg = static_cast<double>(sum) / nums.size();\n    std::cout << "Sum: " << sum << ", Avg: " << avg << std::endl;\n    return 0;\n}\n')
            ],
            "java": [
                ("day01_01_HelloWorldAndVariables.java", 'public class day01_01_HelloWorldAndVariables {\n    public static void main(String[] args) {\n        String name = "Java Developer";\n        int level = 1;\n        System.out.println("Welcome " + name + " - Level: " + level);\n    }\n}\n'),
                ("day01_02_FibonacciSeries.java", 'public class day01_02_FibonacciSeries {\n    public static void main(String[] args) {\n        int n = 10, a = 0, b = 1;\n        System.out.print("Fibonacci (" + n + " terms): ");\n        for (int i = 0; i < n; i++) {\n            System.out.print(a + " ");\n            int next = a + b;\n            a = b;\n            b = next;\n        }\n        System.out.println();\n    }\n}\n')
            ],
            "go": [
                ("day01_01_hello_types.go", 'package main\n\nimport "fmt"\n\nfunc main() {\n    msg := "Hello from Go Daily Practice"\n    fmt.Println(msg)\n}\n'),
                ("day01_02_temperature_converter.go", 'package main\n\nimport "fmt"\n\nfunc cToF(c float64) float64 {\n    return (c * 9.0 / 5.0) + 32.0\n}\n\nfunc main() {\n    c := 25.0\n    fmt.Printf("%.1f C = %.1f F\\n", c, cToF(c))\n}\n')
            ]
        }
    },
    # Day 2: Loops & Iteration
    {
        "day": 2,
        "topic": "Control Flow & Loops",
        "codes": {
            "python": [
                ("day02_01_prime_checker.py", '"""\nDay 2 - Problem 1: Prime Number Checker in Python\n"""\ndef is_prime(n: int) -> bool:\n    if n <= 1: return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0: return False\n    return True\nprint("Primes < 30:", [x for x in range(1, 30) if is_prime(x)])\n'),
                ("day02_02_multiplication_table.py", '"""\nDay 2 - Problem 2: Formatted Multiplication Matrix in Python\n"""\nfor row in range(1, 6):\n    print(" ".join(f"{row*col:3d}" for col in range(1, 6)))\n')
            ],
            "javascript": [
                ("day02_01_fizzbuzz.js", '// Day 2 - Problem 1: Classic FizzBuzz\nfor (let i = 1; i <= 20; i++) {\n  let out = "";\n  if (i % 3 === 0) out += "Fizz";\n  if (i % 5 === 0) out += "Buzz";\n  console.log(out || i);\n}\n'),
                ("day02_02_array_filter.js", '// Day 2 - Problem 2: Array Filtering & Mapping\nconst nums = [12, 45, 68, 23, 89, 90, 34];\nconst evensDoubled = nums.filter(n => n % 2 === 0).map(n => n * 2);\nconsole.log("Evens Doubled:", evensDoubled);\n')
            ],
            "c": [
                ("day02_01_reverse_number.c", '#include <stdio.h>\nlong reverse(long n) {\n    long r = 0;\n    while(n) { r = r*10 + (n%10); n/=10; }\n    return r;\n}\nint main() {\n    printf("Reversed: %ld\\n", reverse(987654321));\n    return 0;\n}\n'),
                ("day02_02_factorial.c", '#include <stdio.h>\nunsigned long long fact(int n) {\n    unsigned long long res = 1;\n    for(int i=2; i<=n; i++) res *= i;\n    return res;\n}\nint main() {\n    printf("10! = %llu\\n", fact(10));\n    return 0;\n}\n')
            ],
            "cpp": [
                ("day02_01_binary_search.cpp", '#include <iostream>\n#include <vector>\nint binarySearch(const std::vector<int>& v, int t) {\n    int l = 0, r = v.size() - 1;\n    while(l <= r) {\n        int m = l + (r - l)/2;\n        if(v[m] == t) return m;\n        if(v[m] < t) l = m + 1; else r = m - 1;\n    }\n    return -1;\n}\nint main() {\n    std::vector<int> arr = {1, 3, 5, 7, 9, 11};\n    std::cout << "Index of 7: " << binarySearch(arr, 7) << std::endl;\n    return 0;\n}\n'),
                ("day02_02_vector_minmax.cpp", '#include <iostream>\n#include <vector>\n#include <algorithm>\nint main() {\n    std::vector<int> v = {45, 12, 89, 34, 67};\n    std::cout << "Min: " << *std::min_element(v.begin(), v.end()) << "\\n";\n    std::cout << "Max: " << *std::max_element(v.begin(), v.end()) << "\\n";\n    return 0;\n}\n')
            ],
            "java": [
                ("day02_01_AnagramChecker.java", 'import java.util.Arrays;\npublic class day02_01_AnagramChecker {\n    public static boolean isAnagram(String s1, String s2) {\n        char[] a = s1.toLowerCase().toCharArray();\n        char[] b = s2.toLowerCase().toCharArray();\n        Arrays.sort(a); Arrays.sort(b);\n        return Arrays.equals(a, b);\n    }\n    public static void main(String[] args) {\n        System.out.println("listen/silent: " + isAnagram("listen", "silent"));\n    }\n}\n'),
                ("day02_02_SecondLargest.java", 'public class day02_02_SecondLargest {\n    public static void main(String[] args) {\n        int[] arr = {10, 45, 23, 89, 67};\n        int m1 = -1, m2 = -1;\n        for(int n : arr) {\n            if(n > m1) { m2 = m1; m1 = n; }\n            else if(n > m2 && n != m1) m2 = n;\n        }\n        System.out.println("Second largest: " + m2);\n    }\n}\n')
            ],
            "go": [
                ("day02_01_slice_rotator.go", 'package main\nimport "fmt"\nfunc rotate(nums []int, k int) []int {\n    k = k % len(nums)\n    return append(nums[len(nums)-k:], nums[:len(nums)-k]...)\n}\nfunc main() {\n    fmt.Println(rotate([]int{1,2,3,4,5}, 2))\n}\n'),
                ("day02_02_word_count.go", 'package main\nimport ("fmt"; "strings")\nfunc main() {\n    text := "go is fast and go is clean"\n    counts := make(map[string]int)\n    for _, w := range strings.Fields(text) { counts[w]++ }\n    fmt.Println(counts)\n}\n')
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

def generate_today():
    today_str = date.today().isoformat()
    state = load_state()

    current_day = state.get("current_day", 1)
    lang_index = state.get("lang_index", 0)

    # Choose language rotating every day
    lang = LANGUAGES[lang_index % len(LANGUAGES)]
    
    curr_item = next((c for c in CURRICULUM if c["day"] == current_day), None)
    if not curr_item:
        curr_item = CURRICULUM[(current_day - 1) % len(CURRICULUM)]

    codes = curr_item["codes"].get(lang, curr_item["codes"]["python"])

    lang_dir = os.path.join(WORKSPACE_DIR, lang)
    os.makedirs(lang_dir, exist_ok=True)

    created_files = []
    for filename, code_content in codes:
        target_path = os.path.join(lang_dir, filename)
        with open(target_path, "w") as f:
            f.write(code_content)
        created_files.append((filename, target_path))
        print(f"📄 Created: {target_path}")

    # Append to README.md table
    table_entry = f"| **{today_str} (Day {current_day})** | `{lang.upper()}` | {curr_item['topic']} | [`{created_files[0][0]}`]({lang}/{created_files[0][0]}), [`{created_files[1][0]}`]({lang}/{created_files[1][0]}) |\n"
    
    if os.path.exists(README_FILE):
        with open(README_FILE, "r") as f:
            readme_content = f.read()
        if "| Date | Language |" in readme_content:
            with open(README_FILE, "a") as f:
                f.write(table_entry)

    state["current_day"] = current_day + 1
    state["lang_index"] = lang_index + 1
    state["history"].append({
        "date": today_str,
        "day": current_day,
        "language": lang,
        "files": [f[0] for f in created_files]
    })
    save_state(state)

    print(f"\n✨ Generated 2 {lang.upper()} exercises for Day {current_day}!")

if __name__ == "__main__":
    generate_today()
