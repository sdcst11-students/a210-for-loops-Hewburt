"""
Help Jenny keep track of her expenses!
Each month, she needs to keep track of:
1. The current balance on her credit card
2. The total amount of her purchases
3. The total amount that she pays off
4. If she has an unpaid balance, then 2% of the current balance is charged to her

Write a program that asks her to enter in her total purchases as
well as how much she pays off.  Calculate any interest that she must add to her
balance and display her total balance at the end of the month.

A sample for the first few months is shown below:

Enter total purchases for month(1) : 100
Enter total payments for month(1)  : 75
2% interest has been charged: 0.5
Your closing balance is $25.5

Enter total purchases for month(2) : 100
Enter total payments for month(2)  : 75
2% interest has been charged: 1.01
Your closing balance is $51.51

"""

current_balance = 0
def calculate_balance(purchases, payments, balance):
    interest = 0
    if balance > 0:
        interest = balance * 0.02
    new_balance = balance + purchases - payments + interest
    return new_balance, interest
for month in range(1, 4):  
    purchases = float(input(f"Enter total purchases for month({month}): "))
    payments = float(input(f"Enter total payments for month({month}): "))
    current_balance, interest_charged = calculate_balance(purchases, payments, current_balance)
    print(f"2% interest has been charged: {interest_charged:.2f}")
    print(f"Your closing balance is ${current_balance:.2f}\n")
