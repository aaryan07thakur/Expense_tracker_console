#Expenses Tracker Project

expensesList=[] #list of all expenses in form of dictionay
print("Welcome to the Expense Tracker!")

while True:
    print("==========MENU==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choise=int(input("Enter your choice (1-4): "))

#1.ADD EXPENSE
    if choise==1:
        date=input("Enter the date (YYYY-MM-DD): ")
        amount=float(input("Enter the amount of expenses: "))
        category=input("Enter the category of expense (e.g., Food, Transport, Utillities, etc.): ")
        description=input("Enter a brief description of the expense: ")

        expenses={
            'date':date,
            'amount':amount,
            'category':category,
            'description':description
        }
        expensesList.append(expenses)
        print("\nExpense added successfully!\n")

#2.VIEW ALL EXPENSES
    elif(choise==2):
        if (len(expensesList)==0):
            print("\nNo expenses recorded yet.\n")
        else:
            print("\n==================All Expenses====================")
            count=1
            for eachexpense in expensesList:
                print(f"ExpensesNumber {count} -->> {eachexpense['date']}, {eachexpense['amount']}, {eachexpense['category']}, {eachexpense['description']}")
                count+=1

#3. VIEW TOTAL EXPENSES
    elif(choise==3):
        total_expenses=0
        for eachexpense in expensesList:
            total_expenses+=eachexpense['amount']
        print(f"\nTotal Expenses: {total_expenses}\n")

#4. EXIT
    elif(choise==4):
        print("Thankyou for using Expenses Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")









