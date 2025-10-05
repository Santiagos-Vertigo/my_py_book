results = {}
numbers = [12, 3, 34, 56, 99, 100]

for n in numbers:
    results[n] = "even" if n % 2 == 0 else "odd"
    print(f"{n} is {results[n]}")

print("Results: ", results)