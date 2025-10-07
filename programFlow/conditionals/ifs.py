def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot

user_input = input("Enter numbers separated by spaces: \n")
numbers = [int(x) for x in user_input.split()]

print("The sum is: \n", multiply_list(numbers))