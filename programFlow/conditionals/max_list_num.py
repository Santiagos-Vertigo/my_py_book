def my_num(numbers):
    num = numbers[0]
    for a in numbers:
        if a %  num and a == 0:
            num *= a
    return num

user_input = input("Enter digits: ")

numbers = [int(x) for x in user_input.split()]

print(f"min number is {my_num(numbers)}")
