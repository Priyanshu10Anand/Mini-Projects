print("""
---- SPECIAL NUMBERS CHECKER ----

1)  Buzz Number: Divisible by 7 or ends with 7.           → e.g., 63 or 67
2)  Armstrong Number: Sum of cubes of digits = number.   → e.g., 153
3)  Perfect Number: Sum of proper divisors = number.     → e.g., 6
4)  Spy Number: Sum of digits = Product of digits.       → e.g., 123 (1+2+3 = 1×2×3)
5)  Niven Number: Divisible by sum of digits.            → e.g., 36
6)  Lead Number: Sum of even digits = Sum of odd digits. → e.g., 2343 or 2451
7)  Duck Number: Has zero(s) but doesn't start with 0.   → e.g., 101 or 1000
8)  Tech Number: Even-digit number where (left+right)² = number. → e.g., 2025
9)  Prime Number: Has only 2 factors — 1 and itself.     → e.g., 5 or 17
10) Palindrome Number: Same forwards and backwards.      → e.g., 12321 or 14141
""")

def is_buzz(n):
    return n % 7 == 0 or str(n).endswith('7')

def is_armstrong(n):
    return n == sum(int(d)**3 for d in str(n))

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_spy(n):
    digits = [int(d) for d in str(n)]
    return sum(digits) == eval('*'.join(str(d) for d in digits))  # same as math.prod

def is_niven(n):
    s = sum(int(d) for d in str(n))
    return s != 0 and n % s == 0

def is_lead(n):
    even_sum = sum(int(d) for d in str(n) if int(d) % 2 == 0)
    odd_sum = sum(int(d) for d in str(n) if int(d) % 2 != 0)
    return even_sum == odd_sum

def is_duck(n):
    s = str(n)
    return '0' in s[1:]

def is_tech(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    left = int(s[:mid])
    right = int(s[mid:])
    return (left + right) ** 2 == n

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]


while True:
    try:
        num = int(input("\n🔢 Enter a number to check: "))
    except ValueError:
        print("⚠️ Please enter a valid integer.")
        continue

    print(f"\n🔍 Results for {num}:")

    print("➡️  Buzz Number:        ", "✅ Yes" if is_buzz(num) else "❌ No")
    print("➡️  Armstrong Number:   ", "✅ Yes" if is_armstrong(num) else "❌ No")
    print("➡️  Perfect Number:     ", "✅ Yes" if is_perfect(num) else "❌ No")
    print("➡️  Spy Number:         ", "✅ Yes" if is_spy(num) else "❌ No")
    print("➡️  Niven Number:       ", "✅ Yes" if is_niven(num) else "❌ No")
    print("➡️  Lead Number:        ", "✅ Yes" if is_lead(num) else "❌ No")
    print("➡️  Duck Number:        ", "✅ Yes" if is_duck(num) else "❌ No")
    print("➡️  Tech Number:        ", "✅ Yes" if is_tech(num) else "❌ No")
    print("➡️  Prime Number:       ", "✅ Yes" if is_prime(num) else "❌ No")
    print("➡️  Palindrome Number:  ", "✅ Yes" if is_palindrome(num) else "❌ No")

    again = input("\n🔁 Do you want to check another number? (y/n): ").strip().lower()
    if again != 'y':
        print("\n👋 Thank you for using Special Number Checker!")
        print("📌 Built by PRIYANSHU ANAND")
        break
