# input statements
salary = float(input())
numDependents = float(input())

# calculate taxes here
stateTax = salary * 0.065
federalTax = salary * 0.28
dependentDeduction = (numDependents * 0.025) * salary
totalWithholding =  stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

# output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))

# Repeating the program

# input statements
salary = float(input())
numDependents = float(input())

# calculate taxes here
stateTax = salary * 0.065
federalTax = salary * 0.28
dependentDeduction = (numDependents * 0.025) * salary
totalWithholding =  stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

# output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))