import time
import random
import math

# Random loading times
randnum1 = random.uniform(1, 5)
randnum2 = random.uniform(1, 5)
randnum3 = random.uniform(1, 5)

# Functions
def calculate_total(price, quantity):
    return price * quantity

def calculate_change(total_cost, payment):
    return payment - total_cost

# First Loading Screen
print("Pip-tan: 'Hey! Hello again! Let me get things set up for you.'")
print("=======================================================")
time.sleep(0.5)
print()
time.sleep(0.5)
print("Loading...")
time.sleep(randnum1)
print(f"Done! [Loaded for {math.ceil(randnum1)} seconds.]")
time.sleep(0.5)
print()
time.sleep(0.5)
print("=======================================================")

# Input Block
time.sleep(0.5)
price = int(input("Pip-tan: 'So, how much does the item cost?' "))
time.sleep(0.5)
quantity = int(input("Pip-tan: 'Now, how much did you buy?' "))

total_cost = calculate_total(price, quantity)

print(f"Pip-tan: 'The total cost is {total_cost}.'")
time.sleep(0.5)
payment = int(input("Pip-tan: 'Okay, now, how much did you pay?' "))
time.sleep(0.5)

change_or_shortage = calculate_change(total_cost, payment)
if change_or_shortage < 0:
    shortage_value = abs(change_or_shortage)
    print(f"Pip-tan: 'Oops! You need {shortage_value} more to pay in full.'")
elif change_or_shortage == 0:
    print("Pip-tan: 'You paid the exact amount! Thank you.'")
    print("0")
else:
    print(f"Pip-tan: 'Here is your change: {change_or_shortage}'")

# Second Loading Screen
print("=======================================================")
time.sleep(0.5)
print()
time.sleep(0.5)
print("Loading...")
time.sleep(randnum2)
print(f"Done! [Loaded for {math.ceil(randnum2)} seconds.]")
time.sleep(0.5)
print()
time.sleep(0.5)
print("=======================================================")

# Counter for easy reading
print("Calculated!")
print("=============================================================")
time.sleep(0.5)
print(f"Item Price: {price}")
time.sleep(0.5)
print(f"Item Quantity: {quantity}")
time.sleep(0.5)
print(f"Total Price: {total_cost}") 
time.sleep(0.5)
print(f"Payment: {payment}")
time.sleep(0.5)
if change_or_shortage < 0:
    print(f"Shortage: {abs(change_or_shortage)}")
else:
    print(f"Change: {change_or_shortage}")

time.sleep(1)
print("=============================================================")
print(" ")

# Final Loading Screen
print("=============================================================")
time.sleep(0.5)
print()
time.sleep(0.5)
print("Tidying up...")
time.sleep(randnum3)
print(f"Done! [Tidied up for {math.ceil(randnum3)} secon-")
print("Pip-tan: 'Wait!'")
time.sleep(0.5)
print("Pip-tan: 'Goodbye, and thank you for using the Canteen Purchase Calculator! <3'")
time.sleep(0.5)
print("Tidying up... (again)")
time.sleep(randnum3)
print(f"Done! [Tidied up for {math.ceil(randnum3)} seconds.]")
time.sleep(0.5)
print()
time.sleep(0.5)
print("=============================================================")

# Documentation Question 1: calculate_total calculates the total cost of the purchase, whilst calculate_change calculates the change of the transaction.
# Documentation Question 2: The parameters do not have a fixed value, while the arguments do.
# Documentation Question 3: It is stored in the variable total_cost, being reused once more in the final counter.
# Documentation Question 4: While the total is very important in change calculation, they must be calculated independently, as the total is vastly different from the change, and to be read easily.