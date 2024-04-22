'''
Amare Diotte
Data Engineering 2024-RTT-107
GLAB 340.4.1 Strings
'''
import typing

# This function has no parameter to returns. All inputs and outputs are made in the terminal
def StringGame() -> None:
    # asks user for a word
    word: str = input("Please enter a word: ").lower()

    # print word to terminal
    print("The length of your word is:", len(word))
    print("Your word in lower case:", word)
    print("Your word in upper case:", word.upper())

    # input letter for count
    letter: chr = input("Enter a letter: ").lower()
    count: int = word.count(letter)
    s_suffix: str = ""
    if count != 1:
        s_suffix = "s" 
    print("The letter '" + letter + "' occurs", count, "time" + s_suffix, "in '" + word + "'")

    # input substring for count
    substring: str = input("Enter a substring: ")
    substring_count: int = word.count(substring)
    if substring_count != 1:
        s_suffix = "s" 
    else:
        s_suffix = ""
    print("The substring '" + substring + "' appears", substring_count, "time" + s_suffix, "in the word '" + word + "'")

    # accessing characters by index
    print("Reverse:", word[::-1])
    starting_index : int = int(input("Please enter a starting index: "))
    ending_index : int = int(input("Please enter an ending index: "))
    if ending_index > len(word):
        print("Invalid index! Skipping to next line")
    else:
        print("Slicing '" + word + "' from index", starting_index, "to", ending_index, "returns :", word[starting_index:ending_index])

    # replacing characters in a string
    print("This is your word:", word)
    old_character : chr = input("Enter a character to replace: ")
    new_character : chr = input("What letter will replace it? ")
    new_word : str = word.replace(old_character, new_character)
    print("Your new word with substituted characters: ", new_word)

    # concatination and palindromes
    second_word : str = input("Enter a second word: ")
    concat_word = word + second_word
    print("Concatenated with your first word:", concat_word)

    print("Is this new word a pallindrome?")
    if concat_word[::] == concat_word[::-1]:
        print("The new word", concat_word, "is a palindrome!")
    else:
        print("The new word", concat_word, "is NOT a palindrome!")

    print("Can this word be used as an identifier?")

    # can the new word be used as and identifier?
    if concat_word.isidentifier():
        print(concat_word, "IS a valid Python Identifier")
    else:
        print(concat_word, "is NOT a valid Python identifier")

StringGame()