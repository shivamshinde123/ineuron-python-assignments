
def reverse_a_word(word):

    return word[::-1]


if __name__ == '__main__':
    word = input("Please enter a word you would like to reverse")
    print(f"Entered word: {word}")
    print(f"Reversed word: {reverse_a_word(word)}")