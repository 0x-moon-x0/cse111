import csv
from datetime import datetime

def main ():

    try:

        products_dict = read_dictionary ("products.csv", 0)

        print ("Inkom Emporium")
        print ()

        with open ("request.csv", "rt") as csv_file:

            reader = csv.reader (csv_file)
            next (reader)

            time = datetime.now ()
            day = time.weekday ()

            items_quantity_list = []
            subtotal_list = []

            for row in reader:

                product_no = row [0]
                quantity = int (row [1])

                if product_no in products_dict:

                    value = products_dict [product_no]
                    name = value [1]
                    price = float (value [2])

                    subtotal_per_item = price * quantity
                    subtotal_list.append (subtotal_per_item)
                    items_quantity_list.append (quantity)
                    
                    items_quantity = sum (items_quantity_list)
                    subtotal = sum (subtotal_list)
                    tax = subtotal * 0.06
                    total = subtotal + tax

                    print (f"{name}: {quantity} @ {price}")

            if day == 1 or day == 2:

                discount = subtotal * 0.1
                discount_subtotal = subtotal - discount
                discount_tax = discount_subtotal * 0.06
                discount_total = discount_subtotal + discount_tax

                print ()
                print (f"Number of Items: {items_quantity}")
                print (f"Subtotal: {discount_subtotal:.2f}")
                print (f"Sales Tax: {discount_tax:.2f}")
                print (f"Total: {discount_total:.2f}")
            
            else:

                print ()
                print (f"Number of Items: {items_quantity}")
                print (f"Subtotal: {subtotal:.2f}")
                print (f"Sales Tax: {tax:.2f}")
                print (f"Total: {total:.2f}")

            print ()
            print ("Thank you for shopping at Inkom Emporium.")
            print (f"{time:%c}")
        
    except (FileNotFoundError, PermissionError) as error:
        print ("Error: missing file")
        print (error)

    except (KeyError) as error:
        print (f"Error: unknown product ID in the {csv_file} file '{product_no}'")


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}

    with open (filename, "rt") as csv_file:

        reader = csv.reader (csv_file)
        next (reader)

        for row_list in reader:

            if row_list != 0:

                key = row_list [key_column_index]
                dictionary [key] = row_list
    
    return dictionary


if __name__ == "__main__":
    main()         