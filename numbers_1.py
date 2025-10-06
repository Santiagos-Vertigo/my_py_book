# #using range function on lists
# numbers = list(range(1, 6))
# print(numbers)


# even_numbers = list(range(0,20, 3))
# print(even_numbers)

# # just simple squares
# squares = []
# for value in range(1, 11):
#     squares.append(value ** 2)
# print(squares)

# # OR using comprehension
# squares_2 = [value ** 2 for value in range(1, 11)]
# print(squares_2)


# #
# digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# digits = [int(digit) for digit in digits]
# print(min(digits))
# print(max(digits))
# print(sum(digits))


#exercise
# 
#count to 20
list_to_20 = list(range(1, 20))
print()
#to a 1000000
list_to_1000000 = list(range(1, 1000000))
# print(list_to_1000000)
#min() and max() and sum
list_min_max_sum = [int(digit) for digit in list_to_1000000]

print(min(list_min_max_sum))
print(max(list_min_max_sum))
print(sum(list_min_max_sum))

# print odd numbers in a loop from 1 to 20

odd_numbers = list(range(1, 21, 3))
print(odd_numbers)
