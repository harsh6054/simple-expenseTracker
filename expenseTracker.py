expenses = {}

def add_expense():
    name = input("Enter expense name: ")
    while True:
        try:
            amount = float(input("Enter expense amount: ₹"))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    expenses[name] = amount
    print(f"Expense '{name}' of ₹{amount:.2f} added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    print("\n--- All Expenses ---")
    total = 0
    for name, amount in expenses.items():
        print(f"{name}: ₹{amount:.2f}")
        total += amount
    print(f"Total Expenses: ₹{total:.2f}\n")

def delete_expense():
    if not expenses:
        print("No expenses to delete.\n")
        return
    name = input("Enter the expense name to delete: ")
    if name in expenses:
        del expenses[name]
        print(f"Expense '{name}' deleted successfully!\n")
    else:
        print(f"No expense found with name '{name}'.\n")

def main():
    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-4.\n")

if __name__ == "__main__":
    main()
