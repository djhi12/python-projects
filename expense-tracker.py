import datetime

# Create a dictionary to store expenses by month and category
expenses = {}


def log_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    date = datetime.datetime.now()
    month_year = date.strftime("%Y-%m")

    if month_year not in expenses:
        expenses[month_year] = {}

    if category not in expenses[month_year]:
        expenses[month_year][category] = 0

    expenses[month_year][category] += amount
    print(
        f"Expense of ${amount:.2f} in the '{category}' category logged for {month_year}.")


def generate_report():
    print("\nExpense Report:")
    for month_year, categories in expenses.items():
        print(f"\n{month_year}:")
        for category, amount in categories.items():
            print(f"{category}: ${amount:.2f}")
        total = sum(categories.values())
        print(f"Total: ${total:.2f}")


def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Log Expense")
        print("2. Generate Report")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            log_expense()
        elif choice == '2':
            generate_report()
        elif choice == '3':
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
