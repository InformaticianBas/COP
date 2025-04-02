# Declarations
employee_name = input("Enter Employee Name: ")
number_of_shifts = input ("Enter number of shifts: ")
number_of_transactions = input("Enter number of transactions: ")
transaction_dollar_value = input("Enter transaction dollar value: ")
productivity_score = int((float(transaction_dollar_value)/float(number_of_transactions))/float(number_of_shifts))
bonus = 0.00

# Calculate bonus based on the inputs with nested ifs
if (productivity_score > 30 ):
    if (productivity_score > 69):
        if (productivity_score >= 200):
            bonus = 200.00
        else:
            bonus = 100.00
    else:
        bonus = 75.00
else:
    bonus = 50.00

# Print the name and calculated bonus 
print(employee_name)
print(bonus)