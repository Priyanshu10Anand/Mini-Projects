# 🔢 Special Number Checker

A Python-based command-line tool to check if a number belongs to various special number categories like Armstrong, Prime, Palindrome, Tech, and more!

---

## 🚀 Features

This tool allows users to check the following **special number types**:

| Number Type       | Description                                                                 | Example      |
|-------------------|-----------------------------------------------------------------------------|--------------|
| **Buzz Number**   | Divisible by 7 or ends with 7                                               | 63, 67       |
| **Armstrong**     | Sum of the cubes of its digits = number itself (for 3-digit numbers)        | 153          |
| **Perfect**       | Sum of proper divisors = number                                             | 6            |
| **Spy Number**    | Sum of digits = Product of digits                                           | 123, 1124    |
| **Niven Number**  | Divisible by sum of its digits                                              | 36, 132      |
| **Lead Number**   | Sum of even digits = Sum of odd digits                                      | 2343, 2451   |
| **Duck Number**   | Has at least one zero (not at the start)                                   | 101, 1000    |
| **Tech Number**   | Even-digit number where (left half + right half)^2 = number                | 2025         |
| **Prime Number**  | Has exactly two factors: 1 and itself                                       | 2, 3, 5, 17  |
| **Palindrome**    | Reads the same forward and backward                                         | 121, 12321   |

---

## 📂 File Structure

```bash
📦special-number-checker
 ┣ 📄 special_number_checker.py  # Main program
 ┗ 📄 README.md                  # Project documentation
