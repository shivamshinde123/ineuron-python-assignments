
def print_in_rev_order(str1, str2):

    print(f"{str1[::-1]} {str2[::-1]}")


if __name__ == '__main__':

    fname = input("Enter your first name")
    lname = input("Enter your last name")

    print_in_rev_order(fname, lname)