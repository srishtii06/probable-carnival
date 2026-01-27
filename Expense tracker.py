import os
import json

class Expense:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

def add_expense(expenses):
    date = input("Enter date (DD-MM-YYYY2): ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    expense = Expense(date, amount, category, description)
    expenses.append(expense)
    print("Expense added successfully!")

def list_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    else:
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. Date: {expense.date}, Amount: {expense.amount}, Category: {expense.category}, Description: {expense.description}")

def calculate_total_expenses(expenses):
    total = sum(expense.amount for expense in expenses)
    print(f"Total Expenses: ${total:.2f}")

def save_data(expenses, filename):
    with open(filename, 'w') as file:
        json.dump([expense.__dict__ for expense in expenses], file)

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            expenses = [Expense(**item) for item in data]
            return expenses
    else:
        return []

def main():
    filename = "expenses.json"
    expenses = load_data(filename)

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Calculate Total Expenses")
        print("4. Save Data")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            calculate_total_expenses(expenses)
        elif choice == "4":
            save_data(expenses, filename)
            print("Data saved successfully!")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
