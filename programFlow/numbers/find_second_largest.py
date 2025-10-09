def find_second_largest(numbers):
    # Step 1: Find the largest
    largest = max(numbers)

    # Step 2: Remove all occurrences of that largest number
    filtered = [n for n in numbers if n != largest]

    # Step 3: Handle edge case — if no second largest exists
    if not filtered:
        return None

    # Step 4: Find second largest
    second_largest = max(filtered)
    return second_largest


user_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

result = find_second_largest(numbers)

if result is not None:
    print(f"The second largest number is: {result}")
else:
    print("There is no second largest number (all numbers are the same).")
