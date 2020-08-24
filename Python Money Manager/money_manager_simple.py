# A helpful Libraries
import pandas as pd

# Try opening the csv file
try:
    # if file found open the file and set the budget column to the budget variable
    df = pd.read_csv("budget.csv", index_col=None)
    budget = df.loc[0, "Budget"]
except FileNotFoundError:
    # If file is not found, set budget to 0 and create a dataframe with our budget and savings
    # Our budget variable
    budget = 0
    df = pd.DataFrame(
        {"Budget": [0]})

# Take user input and store it in an integer
user_intent = ""

while user_intent != "quit":

    user_intent = str.lower(input('''What would you like to do today?
You can type "help" to get commands\n'''))

    if user_intent == "expense":
        expense = int(input("How much did you spend?\n"))
        budget -= expense
        print(f"Expense of BDT {expense} deducted\n")
    elif user_intent == "salary":
        salary = int(input("How much did you get?\n"))
        budget += salary
        print(f"Salary payment of BDT {salary} added\n")
    elif user_intent == "budget":
        print(f"Your current budget is {budget}\n")

    elif user_intent == "quit":
        print("Quitting the application")
        df.loc[0, "Budget"] = budget
        df.to_csv("budget.csv", index=False)
    else:
        print("You typed something wrong.\n")
