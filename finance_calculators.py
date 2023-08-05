
import math

# Two types of financial calculator to choose from
investment = print("Investment - to calculate the amount of interest you'll earn on your investment")
bond = print("Bond - to calculate the amount you'll have to pay on a home loan")

calculator_selected = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower() # Need to converts all characters to lowercase in case the users enter in different way

if calculator_selected == "investment" or calculator_selected == "bond": # Need to limit the input to only two specific words
    print(f"Congratulations, you have chosen {calculator_selected}")
else:
    print("Error! Your input doesn`t meet the requirements. Please enter either 'investment' or 'bond'") # Error message if different


# Interest calculation using two types of calculators

# First type of calculators
if calculator_selected == "investment":
     deposit = float(input("Please enter the amount of money that you are depositing: "))
     interest_investment_rate = float(input("Please enter the interest rate: "))
     investing_years = float(input("Please enter the number of years you plan on investing: "))
     interest_type = input("Which type of interest would you like to use? Please enter 'simple' or 'compound'").lower() # Need to converts all characters to lowercase in case the users enter in different way
     
     # Two types of interest used in the investment calculator
     if interest_type == "simple":
        total_simple_int_amount = int(deposit*(1+(interest_investment_rate/100)*investing_years))
        print(f"Your total amount of money received from the simple rate of investment is ${total_simple_int_amount}")

     elif interest_type == "compound":
        total_compound_int_amount = int(deposit * math.pow((1+(interest_investment_rate/100)), investing_years))
        print(f"Your total amount of money received from the compound rate of investment is ${total_compound_int_amount}")

     else: 
        print("Error! Your input doesn`t meet the requirements. Please enter either 'simple' or 'compound'") # Error message if different

# Second type of calculators   
if calculator_selected == "bond":
     house_value = float(input("Please enter the present value of the house: "))
     interest_bond_rate = float(input("Please enter the interest rate: "))
     repay_months = int(input("Please enter the number of months you plan to take to repay the bond: "))
     repayment = int((((interest_bond_rate/100)/12)*house_value) / (1 - (1 + ((interest_bond_rate/100)/12))**(-repay_months)))
     print(f"Your total amount of money you need to repay each month is ${repayment}")

     




