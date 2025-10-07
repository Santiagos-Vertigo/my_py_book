def find_mode(numbers):
    counts = {}
    for n in numbers:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1
    
    max_count = 0
    mode = None
    for num, count in counts.items():
        if count > max_count:
            max_count = count
            mode = num
    return mode, max_count
    

numbers = [1, 2, 3, 3, 4]
mode, times = find_mode(numbers)
print(f"The number that appears the most is: {mode} ({times} time(s)")

