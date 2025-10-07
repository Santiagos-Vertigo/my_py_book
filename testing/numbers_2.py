my_list = []

for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        my_list.append(str(x))

print(','.join(my_list))