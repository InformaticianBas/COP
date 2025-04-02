# Declarations
employee_name = input("Enter Employee Name: ")
number_of_shifts = input ("Enter number of shifts: ")
number_of_transactions = input("Enter number of transactions: ")
transaction_dollar_value = input("Enter transaction dollar value: ")
productivity_score = ((int(transaction_dollar_value)/int(number_of_transactions))/int(number_of_shifts))
bonus = 0.00

# Calculate bonus with nested ifs
if (productivity_score > 30 ):
    if (productivity_score > 70):
        if (productivity_score > 200):
            bonus = 200.00
        else:
            bonus = 100.00
    else:
        bonus = 75.00
else:
    bonus = 50

#
print(employee_name)
print(bonus)