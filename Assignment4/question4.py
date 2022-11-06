

def confirm_vowel(character):

    if len(character) == 1:
        return character.lower() in ['a','e','i','o','u']
    
    else:
        print("Please enter a single character.")

    

output = confirm_vowel('a')
print(output)