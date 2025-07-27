#Emi calculate
car_price = 1753560
down_payment =int(input("Enter down paymeng Amount"))
bank_interest = 9.0
loan_period = float(input ("Enter Loan peroid"))
loan_amount =car_price - down_paymentmonthly_emi = bank_interest /(12*100)
num_monthes = int(loan_period*12)
emi=loan_amoun * monthly_emi * ((1 + monthly_emi ** num_monthes / (1+monthly_emi) ** num_monthes-1)
print(loan_amount)
print(monthly_emi)                        
