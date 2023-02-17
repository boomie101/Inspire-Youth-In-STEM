#write a program that calculates 16% tax
#earning btw 100k - 150k
#19% tax income is btw 150k - 300k
#30% tax income is above 300k
#5% tax income is less than 100k
#print gross income , net income
income = 90000
tax = 0.16 * 90000
net_income = (income - tax)
print(net_income)

income = 200000
tax = 0.19 * 200000
net_income = (income - tax)
print(net_income)

income = 10000
tax = 0.19
if(income < 20000):
    print("You can earn more")
else:
    print("You are satisfied")

income = 500000
tax = 0.30 * 500000
net_income = (income - tax)
print(net_income)

income = 50000
tax = 0.05 * 50000
net_income = (income - tax)
print(net_income)

income = 1000000
tax = 0.50
if(income > 90000):
    print("You are rich")
else:
    print("You are poor")
income = 60000
tax = 0.25
if(income <= 10000):
    print("You are young")
else:
    print("You are a parent")