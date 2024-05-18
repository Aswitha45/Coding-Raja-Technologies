class BudgetTracker:
    def __init__(self):
        self.income = 0
        self.expenses = {}
        self.categories = set()

    def add_income(self, amount):
        self.income += amount

    def add_expense(self, category, amount):
        if category not in self.expenses:
            self.expenses[category] = 0
        self.expenses[category] += amount
        self.categories.add(category)

    def calculate_remaining_budget(self):
        total_expenses = sum(self.expenses.values())
        remaining_budget = self.income - total_expenses
        return remaining_budget

    def display_spending_trends(self):
        print("\nSpending Trends:")
        for category in self.categories:
            print(f"{category}: ${self.expenses.get(category, 0)}")

if __name__ == "__main__":
    budget_tracker = BudgetTracker()

    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Remaining Budget")
        print("4. Display Spending Trends")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            income_amount = float(input("Enter income amount: $"))
            budget_tracker.add_income(income_amount)
            print(f"Income added: ${income_amount}")
        elif choice == "2":
            expense_category = input("Enter expense category: ")
            expense_amount = float(input("Enter expense amount: $"))
            budget_tracker.add_expense(expense_category, expense_amount)
            print(f"Expense added ({expense_category}): ${expense_amount}")
        elif choice == "3":
            remaining_budget = budget_tracker.calculate_remaining_budget()
            print(f"Remaining Budget: ${remaining_budget}")
        elif choice == "4":
            budget_tracker.display_spending_trends()
        elif choice == "5":
            print("Exiting Budget Tracker. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
