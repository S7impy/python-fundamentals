'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
amount = int(input("Please enter your investment amount: "))
rate = int(input("Please enter interest rate percentage: "))
years = int(input("Please provide number of years to invest: "))

amount_x = amount * ((1 + rate / 100) ** years)

print(f"Your invested amount will increase to {amount_x} after {years} years")