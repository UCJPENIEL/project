import json 

# initialise expense list
expenses = []

# --Load expenses when the programme starts
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
    print("Expenses loaded successfully!")
except FileNotFoundError:
    print("No saved expenses found. starting fresh.")

while True:
    print("\n--- Expense Tracker Menu ---")
    print("1. Add an expense")
    print("2. View expenses")
    print("3. Calculate total expenses")
    print("4. Calculate expense by category")
    print("5. Delete an expense")
    print("6. Save expense to a file")
    print("7. Exit")
    
    choice = input("Choose an option (1-7): ")
    
    # Add an expense using the provided input
    if choice == "1":
        amount = float(input("Enter the amount of the expense: "))
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        category = input("Enter the category of the expense(transportation, food, entertainment, etc.): ")
        description = input("Enter a description of the expense: ")

        # Store variable inside the dictionary
        expense = {
            "amount": amount,
            "date": date,
            "category": category.lower(),
            "description": description
        }

        expenses.append(expense)
        print("Expense added successfully!")

    # 2. View all expenses
    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        for idx, exp in enumerate(expenses, 1):
            print(f"{idx}. {exp['date']} | {exp['category'].title()} | ₦{exp['amount']} | {exp['description']}")
            
    # 3. Calculate total spending
    elif choice == "3":
        total = sum(exp['amount'] for exp in expenses)
        print(f"Total spending: ₦{total:.2f}")
        
    # 4. Calculate spending by category
    elif choice == "4":
        search_cat = input("Enter the category to calculate: ").lower()
        cat_total = sum(exp['amount'] for exp in expenses if exp['category'] == search_cat)
        print(f"Total spent on {search_cat}: ₦{cat_total:.2f}")
        
    # 5. Delete an expense
    elif choice == "5":
        if not expenses:
            print("No expenses to delete.")
            continue
        # Show options to user so they know what index to choose
        for idx, exp in enumerate(expenses, 1):
            print(f"{idx}. {exp['description']} (₦{exp['amount']})")
            
        del_idx = int(input("Enter the number of the expense to delete: ")) - 1
        if 0 <= del_idx < len(expenses):
            removed = expenses.pop(del_idx)
            print(f"Deleted: {removed['description']}")
        else:
            print("Invalid option.")
            
    # 6. Save expenses to a file
    elif choice == "6":
        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)
        print("Expenses saved to expenses.json!")
        
    # 7. Exit the program
    elif choice == "7":
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice. Please select a number between 1 and 7.")   

