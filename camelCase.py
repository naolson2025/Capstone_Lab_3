#Write a program that turns a sentence into camel case. 
#The first word is lowercase, the rest of the words have their initial letter capitalized, and all of the words are joined together. 
#For example, with the input "fOnt proCESSOR and ParsER", your program will output "fontProcessorAndParser". 
#Optional: can you do this with a list comprehension?
#Optional extra question: print a warning message if the input will not produce a valid variable name. 
#You don't need to be exhaustive in checking, but test for a few common issues, such as starting with a number, or 
#containing invalid characters such as # or + or ". 
#Test your program, and comment your code. 

import re

def camel_case(sentence):
    if sentence != '':
        # Split text into a list (found .split on stackoverflow)
        user_input_list = sentence.split()
        # check for numbers and remove them (regular expression found on stackoverflow)
        user_input_list = [word for word in user_input_list if bool(re.search(r'\d', word)) == False]

        if len(user_input_list) != 0:
            # Remove the first word from the list and make it all lower case (Found .pop on stackoverflow)
            camelCase = user_input_list.pop(0).lower()

            # Capitalize each word then add them to the camelCase (.capitalize found on geeks for geeks)
            for word in user_input_list:
                word = word.capitalize()
                camelCase = camelCase + word

            return camelCase
        else:
            return ''
    else:
        return sentence

def main():
    # Gather text from user
    sentence = input("Enter a sentence to have it adjusted to camelCase. All words with digits will be removed.: ")
    camelCased = camel_case(sentence)
    print(camelCased)

if __name__ == '__main__':
    main()