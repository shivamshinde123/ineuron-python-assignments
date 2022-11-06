

def find_length(lst):

    len_of_words_in_lst = []

    try:
        if type(lst) is list:
            for word in lst:
                len_of_words_in_lst.append(len(str(word)))

            return len_of_words_in_lst
        
    except Exception as e:
        print(e)
        raise e

output = find_length(["ab","cde","erty"])
print(output)
