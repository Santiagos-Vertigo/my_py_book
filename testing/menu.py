while True:
    print("\n=== Main Menu ===")
    print("1. Say Hello")
    print("2. Add Two Numbers")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print("Hello, world!")
    elif choice == "2":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum:", a + b)
    elif choice == "3":
        print("Goodbye!")
        break  # exit the loop
    else:
        print("Invalid option, please try again.")
