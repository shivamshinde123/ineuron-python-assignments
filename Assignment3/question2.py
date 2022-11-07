

def myfilter(func,sequence):
    lst = []
    for item in sequence:
        if func(item):
            lst.append(item)
        else:
            pass
    
    return lst

    
# function that filters vowels
def vowel_filter(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

filtered = myfilter(vowel_filter,sequence)

print("The filtered letters are:")
for item in filtered:
    print(item)