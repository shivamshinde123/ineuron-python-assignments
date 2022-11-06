
def div_by_7_but_not_by_5():

    for num in range(2000,3201):

        if (num % 7 == 0) & (num % 5 != 0):
            print(num, end=", ")

        
div_by_7_but_not_by_5()

