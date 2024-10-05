from datetime import datetime

price = 1
subtotal = 0

print ("Enter the price and quantity for each item.")
print ()

while price != 0:

    price = float (input ("Please enter the price: "))

    if price != 0:

        quantity = int (input ("Please enter the quantity: "))
        subtotal += price * quantity
        print ()

date_and_time = datetime.now ()
weekday = date_and_time.weekday ()

if subtotal >= 50 and (weekday == 1 or weekday == 2):

    discount = subtotal * 0.10
    print (f"Discount amount: {discount:.2f}")
    subtotal -= discount

elif subtotal < 50 and (weekday == 1 or weekday == 2):

    difference = 50 - subtotal
    print (f"You only need {difference} more to receive a 10% discount today!")

sales_tax = subtotal * 0.06
print (f"Sales tax amount: {sales_tax:.2f}")

total = subtotal + sales_tax
print (f"Total: {total:.2f}")
