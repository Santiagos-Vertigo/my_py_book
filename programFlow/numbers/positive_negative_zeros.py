def count_signs(numbers):
    positive = 0
    negative = 0
    zero = 0

    for n in numbers:
        if n > 0:
            positive += 1
        elif n < 0:
            negative += 1
        else:
            zero += 1
    return positive, negative, zero

user_input = input(f"Enter a list positives, negatives and zeros: ")

numbers = [int(x) for x in user_input.split()]
pos, neg, zer = count_signs(numbers)

print(f"Positives: {pos}")
print(f"Negatives: {neg}")
print(f"Zeros: {zer}")