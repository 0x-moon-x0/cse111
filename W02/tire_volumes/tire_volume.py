from datetime import datetime
import math

width = int (input ("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int (input ("Enter the aspect ratio of the tire (ex 60): "))
diameter = int (input ("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

print ()
print (f"The approximate volume is {volume:.2f} liters")

print ()
buy_tires = input ("Would you like to buy tires with the dimensions that you've entered? (y/n) ")

date_and_time = datetime.now ()

if buy_tires.lower () == "y" or buy_tires.lower() == "yes":

    print ()
    phone_number = int (input ("Please enter your phone number: "))

    with open ("volumes.txt", mode = "a") as volumes_file:

        print (f"{date_and_time:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, {phone_number}", file = volumes_file)

else:
    
    with open ("volumes.txt", mode = "a") as volumes_file:

        print (f"{date_and_time:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}", file = volumes_file)