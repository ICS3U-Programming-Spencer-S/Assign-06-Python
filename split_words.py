#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Dec 19, 2022
# This is a program which accepts a list of words
# Then displays the odds words in the list


# function definition
def split_words(input_strs):
    # splits the list
    words = input_strs.split()

    # creates an empty list for later
    odd_words = []

    # for loop to run though until it's out of words
    for i, word in enumerate(words):

        # to determine if a word is odd
        if i % 2 == 0:
            # appends to the above list
            odd_words.append(word)

    # returns to the main function
    return odd_words


def main():
    # intro text
    print("This is a program which accepts a line of strings")
    print("before finding the odd words in the line")
    print("")

    # obtains user input
    input_raw = input("Enter a line of words: ")

    # strips the above input for only words
    input_strs = input_raw.strip()

    # calls the above function into use
    odd_words = split_words(input_strs)
    # using len, check to see if no words were inputted
    if len(odd_words) == 0:
        wait = input("You inputted zero words, press enter to continue.")
    # end correct output
    else:
        print("The odd elements are:", odd_words)


if __name__ == "__main__":
    # looping the program after it's complete
    main()
    answer = input("Would you like to restart? (y/n): ")
    while answer == "y":
        main()
        answer = input("Would you like to restart? (y/n): ")
