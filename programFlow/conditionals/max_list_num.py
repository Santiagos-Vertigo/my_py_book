def max_num(numbers):
    max = 0
    for n in numbers:
        if n > max:
            max = a
    return max

usuer_input = input("enter numbers: ")

numbers = [int(x) for x in usuer_input.split()]

print(f"these are the even numbers: {max_num(numbers)} ")