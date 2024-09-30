"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

SALES_THRESHOLD = 1000
sales = float(input("Enter sales: $"))
if sales >= SALES_THRESHOLD:
    bonus = sales * 0.15
else:
    bonus = sales * 0.10
print(f"Your bonus is ${bonus}")
