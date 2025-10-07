def odds(numbers):
    odd_count = 0
    for n in numbers:
        if n % 2 == 0 :
            odd_count += 1
    return odd_count

def even(numbers):
    even_count = 0
    for i in numbers:
        if i % 2 != 0:
            even_count += 1
    return even_count

user_input = input("input numbers: ")

numbers = [int(x) for x in user_input.split()]

print(f"these are the odd numbers{odds(numbers)}")
print(f"these are the even numbers{even(numbers)}")