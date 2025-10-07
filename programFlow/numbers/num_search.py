def search_num(numbers, target):
    found = False
    for n in numbers:
        if n == target:
            found = True
            break
    return found

user_input = input("Enter a list of number separated by spaces: ")
numbers = [int(x) for x in user_input.split()]
print(numbers)

target = int(input("Enter number to search for: "))

if search_num(numbers, target):
    print(f"{target} is in list")
else:
    print(f"{target} not in list")