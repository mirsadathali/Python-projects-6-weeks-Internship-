import os
import json
from datetime import datetime
from collections import defaultdict

class ExpenseTracker:
    def __init__(self, data_file="expenses.json"):
        self.data_file = data_file
        self.expenses = self.load_expenses()

    def load_expenses(self):
        """Load expenses from a file or initialize an empty structure."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error reading expenses file. Starting fresh.")
        return defaultdict(list)

    def save_expenses(self):
        """Save the current expenses to a file."""
        with open(self.data_file, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, description, category):
        """Add a new expense entry."""
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount should be greater than zero.")
        except ValueError as e:
            print(f"Invalid amount: {e}")
            return

        date = datetime.now().strftime("%Y-%m-%d")
        expense = {"amount": amount, "description": description, "category": category}
        self.expenses[date].append(expense)
        self.save_expenses()
        print("Expense added successfully.")

    def view_expenses(self):
        """Display all expenses grouped by date."""
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        for date, entries in self.expenses.items():
            print(f"\nDate: {date}")
            for entry in entries:
                print(f"  - {entry['description']} | ${entry['amount']} | {entry['category']}")

    def monthly_summary(self):
        """Display monthly expense summary and category-wise totals."""
        monthly_totals = defaultdict(float)
        category_totals = defaultdict(float)

        for date, entries in self.expenses.items():
            month = date[:7]  # Extract "YYYY-MM" from "YYYY-MM-DD"
            for entry in entries:
                monthly_totals[month] += entry["amount"]
                category_totals[entry["category"]] += entry["amount"]

        print("\nMonthly Summary:")
        for month, total in monthly_totals.items():
            print(f"  - {month}: ₹{total:.2f}")

        print("\nCategory-wise Totals:")
        for category, total in category_totals.items():
            print(f"  - {category}: ₹{total:.2f}")

    def run(self):
        """Run the Expense Tracker."""
        print("Welcome to Expense Tracker!")
        while True:
            print("\nOptions:")
            print("1. Add an expense")
            print("2. View all expenses")
            print("3. View monthly summary")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                try:
                    amount = input("Enter amount: ₹")
                    description = input("Enter description: ")
                    category = input("Enter category (e.g., Food, Transport, Entertainment): ")
                    self.add_expense(amount, description, category)
                except Exception as e:
                    print(f"Error adding expense: {e}")
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.monthly_summary()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
