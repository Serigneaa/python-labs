# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.



invest = None
interest = None
invest_years = None

while invest == None:
    invest = input("Enter the investment amount: ")
    invest = int(invest)

while interest == None:
    interest = input("Enter the interest rate in percentage: ")
    interest = int(interest)

while invest_years == None:
    invest_years = input("Enter the number of years to invest: ")
    invest_years = int(invest_years)

values = invest*interest*invest_years
print(values)

# Done
