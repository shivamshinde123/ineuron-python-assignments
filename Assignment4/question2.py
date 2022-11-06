

def filter_long_words(lst,n):

    words_longer_than_n = []

    try:
        if type(lst) is list:
            for item in lst:
                if len(str(item)) > n:
                    words_longer_than_n.append(item)
            return words_longer_than_n
    
        else:
            print("ERROR OCCURED:")
            print("Pleaes provide the list and in integer to compare to length of words in list")

    except Exception as e:
        print(e)
        raise e

    
output = filter_long_words(["ab","cde","erty"],2 )
print(output)