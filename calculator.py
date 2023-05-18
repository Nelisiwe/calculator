import math

def investment_calculator():
    amount = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years you plan on investing for: "))
    interest_type = input("Do you want simple or compound interest? ")
    if interest_type == "Simple":
        total_amount = amount * (1 + interest_rate / 100) ** years
    elif interest_type == "Compound":
        total_amount = amount * math.pow((1 + interest_rate / 100), years)
    
    print("The total amount after {} years is {}.".format(years, total_amount))

def bond_calculator():
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate: "))
    months = int(input("Enter the number of months you plan to take to repay the Bond: "))
    monthly_repayment = (interest_rate * present_value) / (1 - (1 + interest_rate) ** (-months))

    print("The monthly repayment amount is {}.".format(monthly_repayment))

print("Welcome to the financial calculators!")
calculation = input("Do you want to calculate an Investment or a Bond? ")
if calculation in ["Investment", "Bond"]:
    if calculation == "Investment":
        investment_calculator()
    elif calculation == "Bond":
        bond_calculator()
else:
    print("Invalid input.")