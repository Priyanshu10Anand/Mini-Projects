def string_functions():
    a = input("Enter a string: ")
    functions = {
        1: len,
        2: lambda s: s.capitalize(),
        3: lambda s: s.count(input("Substring to count: ")),
        4: lambda s: s.find(input("Substring to find: ")),
        5: lambda s: s.index(input("String to find index of: ")),
        6: str.isalnum,
        7: str.isalpha,
        8: str.isdigit,
        9: str.islower,
        10: str.isupper,
        11: str.isspace,
        12: str.upper,
        13: str.lower,
        14: str.lstrip,
        15: str.rstrip,
        16: str.strip,
        17: lambda s: s.startswith(input("Check startswith: ")),
        18: lambda s: s.endswith(input("Check endswith: ")),
        19: str.istitle,
        20: str.title,
        21: lambda s: s.replace(input("Old: "), input("New: ")),
        22: lambda s: input("Symbol to join with: ").join(s),
        23: lambda s: s.split(input("Split by: ")),
        24: lambda s: s.partition(input("Partition by: ")),
        25: str.swapcase,
        26: lambda s: s + input("String to concatenate: "),
        27: lambda s: s * int(input("Repetition count: "))
    }

    print("\nAvailable string operations:")
    for i, f in enumerate(functions, 1):
        print(f"{i}. {functions[i].__name__ if hasattr(functions[i], '__name__') else f'Custom operation {i}'}")

    choice = int(input("\nEnter your choice: "))
    print("\nResult:", functions.get(choice, lambda x: "Invalid choice")(a))


def list_functions():
    try:
        a = eval(input("Enter a list (e.g., [1, 2, 'a']): "))
    except Exception:
        print("Invalid list.")
        return

    print("""
    1: len()
    2: list()
    3: index()
    4: append()
    5: extend()
    6: insert()
    7: pop()
    8: clear()
    9: count()
    10: reverse()
    11: sort()
    12: sorted()
    13: min()
    14: max()
    15: sum()
    16: remove()
    17: concatenation
    18: repetition
    """)

    ch = int(input("Enter your choice: "))
    try:
        if ch == 1:
            print(len(a))
        elif ch == 2:
            b = input("Enter an iterable: ")
            print(list(b))
        elif ch == 3:
            item = input("Enter item to find index: ")
            print(a.index(eval(item)))
        elif ch == 4:
            item = eval(input("Item to append: "))
            a.append(item)
            print(a)
        elif ch == 5:
            items = eval(input("List to extend: "))
            a.extend(items)
            print(a)
        elif ch == 6:
            index = int(input("Index: "))
            value = eval(input("Value: "))
            a.insert(index, value)
            print(a)
        elif ch == 7:
            print("Removed:", a.pop())
            print(a)
        elif ch == 8:
            a.clear()
            print(a)
        elif ch == 9:
            item = eval(input("Item to count: "))
            print(a.count(item))
        elif ch == 10:
            a.reverse()
            print(a)
        elif ch == 11:
            a.sort()
            print(a)
        elif ch == 12:
            print(sorted(a))
        elif ch == 13:
            print(min(a))
        elif ch == 14:
            print(max(a))
        elif ch == 15:
            print(sum(a))
        elif ch == 16:
            item = eval(input("Item to remove: "))
            a.remove(item)
            print(a)
        elif ch == 17:
            b = eval(input("List to concatenate: "))
            print(a + b)
        elif ch == 18:
            times = int(input("Repetition count: "))
            print(a * times)
        else:
            print("Invalid choice.")
    except Exception as e:
        print("Error:", e)


def tuple_functions():
    try:
        a = eval(input("Enter a tuple (e.g., (1, 2, 3)): "))
    except Exception:
        print("Invalid tuple.")
        return

    print("""
    1: len()
    2: tuple()
    3: index()
    4: count()
    5: sorted()
    6: min()
    7: max()
    8: sum()
    9: concatenation
    10: repetition
    """)

    ch = int(input("Enter your choice: "))
    try:
        if ch == 1:
            print(len(a))
        elif ch == 2:
            b = input("Enter iterable: ")
            print(tuple(b))
        elif ch == 3:
            item = eval(input("Item to find index: "))
            print(a.index(item))
        elif ch == 4:
            item = eval(input("Item to count: "))
            print(a.count(item))
        elif ch == 5:
            print(sorted(a))
        elif ch == 6:
            print(min(a))
        elif ch == 7:
            print(max(a))
        elif ch == 8:
            print(sum(a))
        elif ch == 9:
            b = eval(input("Tuple to concatenate: "))
            print(a + b)
        elif ch == 10:
            times = int(input("Repetition count: "))
            print(a * times)
        else:
            print("Invalid choice.")
    except Exception as e:
        print("Error:", e)


def dict_functions():
    try:
        size = int(input("How many students? "))
        a = {input("Roll no: "): int(input("Marks: ")) for _ in range(size)}
    except Exception:
        print("Invalid input.")
        return

    print("""
    1: len()
    2: get()
    3: items()
    4: keys()
    5: values()
    6: min()
    7: max()
    8: sum()
    9: sorted()
    10: clear()
    11: pop()
    12: popitem()
    13: copy()
    14: update()
    15: setdefault()
    16: fromkeys()
    """)

    ch = int(input("Enter your choice: "))
    try:
        if ch == 1:
            print(len(a))
        elif ch == 2:
            key = input("Key to get: ")
            print(a.get(key))
        elif ch == 3:
            print(a.items())
        elif ch == 4:
            print(a.keys())
        elif ch == 5:
            print(a.values())
        elif ch == 6:
            print(min(a))
        elif ch == 7:
            print(max(a))
        elif ch == 8:
            print(sum(a.values()))
        elif ch == 9:
            print(sorted(a.items()))
        elif ch == 10:
            a.clear()
            print(a)
        elif ch == 11:
            key = input("Key to pop: ")
            print(a.pop(key))
        elif ch == 12:
            print(a.popitem())
        elif ch == 13:
            print(a.copy())
        elif ch == 14:
            updates = {input("Key: "): input("Value: ") for _ in range(int(input("How many entries to update? ")))}
            a.update(updates)
            print(a)
        elif ch == 15:
            key = input("Key: ")
            value = input("Value: ")
            print(a.setdefault(key, value))
        elif ch == 16:
            keys = input("Enter comma-separated keys: ").split(",")
            value = input("Value for all keys: ")
            print(dict.fromkeys(keys, value))
        else:
            print("Invalid choice.")
    except Exception as e:
        print("Error:", e)


def main():
    print("Welcome to Python Built-in Function Explorer!")
    name = input("Enter your name: ")
    print(f"\nHello {name} 👋! What do you want to explore today?\n")

    while True:
        print("\nChoose a category:")
        print("1. String Functions")
        print("2. List Functions")
        print("3. Tuple Functions")
        print("4. Dictionary Functions")
        print("5. Exit")

        try:
            choice = int(input("Enter choice (1–5): "))
            if choice == 1:
                string_functions()
            elif choice == 2:
                list_functions()
            elif choice == 3:
                tuple_functions()
            elif choice == 4:
                dict_functions()
            elif choice == 5:
                print(f"\nThank you, {name}. Powered by Priyanshu Anand.")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
