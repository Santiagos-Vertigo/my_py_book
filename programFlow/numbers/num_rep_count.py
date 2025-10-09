
def find_reps(numbers):
    counts = {}
    for n in numbers:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1

    print("Repeated Numbers: ")
    found_any = False
    for num, count in counts.items():
        if count > 1:
            print(f"{num} appears {count} time(s)")
            found_any = True
    
    if not found_any:
        print("No repeated number found.")




user_input = input("enter a list of number separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

find_reps(numbers)