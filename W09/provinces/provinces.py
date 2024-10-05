def main ():

    provinces_list = read_list ("provinces.txt")

    print (provinces_list)

    provinces_list.pop (0)
    provinces_list.pop ()

    for i in range (len (provinces_list)):

        if provinces_list [i] == "AB":

            provinces_list [i] = "Alberta"
    
    count = provinces_list.count ("Alberta")
    
    print()
    print(f"Alberta occurs {count} times in the modified list.")

def read_list (filename):
    """Read the contents of a text file into a list
    and return the list that contains the lines of text.

    Parameter filename: the name of the text file to read
    Return: a list of strings"""

    text_list = []

    with open (filename, "rt") as text_file:

        for line in text_file:

            line = line.strip ()

            text_list.append (line)
    
    return text_list

if __name__ == "__main__":
    main()