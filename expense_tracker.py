# ==========================================
# Python Expense Tracker
# Module 2 - Python Mini Project
# ==========================================

expenses = []


# Function to add an expense
def add_expense():
    print("\n--- Add Expense ---")

    category = input("Enter expense category: ")
    description = input("Enter expense description: ")

    try:
        amount = float(input("Enter expense amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        expense = {
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


# Function to view all expenses
def view_expenses():
    print("\n--- All Expenses ---")

    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['category']} | "
            f"{expense['description']} | "
            f"₹{expense['amount']:.2f}"
        )


# Function to calculate total expenses
def total_expenses():
    total = sum(expense["amount"] for expense in expenses)

    print("\n--- Total Expenses ---")
    print(f"Total spending: ₹{total:.2f}")


# Function to show category-wise expenses
def category_summary():
    print("\n--- Category Summary ---")

    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")


# Main program
def main():
    while True:
        print("\n==============================")
        print("       EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


# Start the program
if __name__ == "__main__":
    main()
