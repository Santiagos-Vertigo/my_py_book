age = int(input("Your age is? : "))

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 30
else:
    price = 40

print(f"Your admission price is ${price}")