# A Helpful Libraries
import pandas as pd

# Try opening the csv file
try:
    # if file found open the file and set the budget column to the budget variable
    df = pd.read_csv("budget.csv", index_col=None)
    budget = df.loc[0, "Budget"]
    lifetime_savings = df.loc[0, "Lifetime_Savings"]
except FileNotFoundError:
    # If file is not found, set budget to 0 and create a dataframe with our budget and savings
    # Our budget variable
    budget = 0
    # lifetime_savings
    lifetime_savings = 0
    df = pd.DataFrame(
        {"Budget": [0], "Lifetime_Savings": [0]})


# Monthly Salary
salary = 30000

# Take user input and store it in an integer
user_intent = ""

while user_intent != "quit":
    if budget < 0:
        print("You're over your budget. Setting it to previous value. Please retype your transactions.")
        budget = df.loc[0, "Budget"]

    user_intent = str.lower(input('''What would you like to do today?
You can type "help" to get commands\n'''))

    if user_intent == "help":
        print('''
        List of commands: 
        "expense" : Type out expenditure and automatically deducts it from your budget
        "salary" : Adds salary to your budget
        "gig" : Type out your gig payment and adds it to your budget
        "quit" : Quits the program
        "budget" : Tells you how much money you have left
        "save" : Transfers money from budget to lifetime savings
        ''')
    elif user_intent == "expense":
        expense = int(input("How much did you spend?\n"))
        budget -= expense
        print(f"Expense of BDT {expense} deducted\n")
    elif user_intent == "salary":
        budget += salary
        print("Salary added\n")
    elif user_intent == "gig":
        gig = int(input("How much did you get?\n"))
        budget += gig
        print(f"Gig payment of BDT {gig} added\n")
    elif user_intent == "budget":
        print(f"Your current budget is {budget}\n")
    elif user_intent == "save":
        saved = int(
            input("How much would you like to transfer to lifetime savings?\n"))
        lifetime_savings += saved
        budget -= saved
        print(f"You transfered BDT {saved} to savings\n")
    elif user_intent == "quit":
        print("Quitting the application")
        df.loc[0, "Budget"] = budget
        df.loc[0, "Lifetime_Savings"] = lifetime_savings
        df.to_csv("budget.csv", index=False)
    else:
        print("Please refer to the help command and check if you made a typo.\n")
