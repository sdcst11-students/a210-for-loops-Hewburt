#! python3
"""
###### Task 2
Ask the user to enter in the prices of 5 items in dollars.cents (eg 10.34).  Find the total value of all items and then calculate the total price including 5% GST and 7% PST

Sample:
Enter in price of item #1: 10.25
Enter in price of item #2: 11.45
Enter in price of item #3: 13.85
Enter in price of item #4: 9.25
Enter in price of item #5: 10.25
Your subtotal is 55.05
Your GST is 2.75
Your PST is 3.85
Your total is 61.65
"""

total_price = 0
for i in range(1, 6):
    price = float(input(f"Enter in price of item #{i}: "))
    total_price += price
gst = total_price * 0.05
pst = total_price * 0.07
total = total_price + gst + pst
print(f"Your subtotal is {total_price:.2f}")
print(f"Your GST is {gst:.2f}")
print(f"Your PST is {pst:.2f}")
print(f"Your total is {total:.2f}")
