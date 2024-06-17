'''Here is the code for password generator in python language
Basses on concept such as 
1.Module-Random
2.string
3.operators
4.Basic concept'''

#The "import random" random module that helps to generate random things such as numbers,alphabets and symbols.

import random

'''The import string statement in Python imports the string module, which contains a collection of string-related utilities. These utilities include constants and functions that are useful for various string operation'''

import string

print("WELCOME TO CODSOFT PASSWORD GENERATOR")

#Defining the length of password
lenght=int(input("Enter the length of password:"))

# According to user's desire
lower_case=int(input("No of lower case u want in password:"))
upper_case=int(input("No of upper case you want in password:"))
digits_pass=int(input("No of digit you want in password:"))
symbols_pass=input("No of symbols you want in password:")


'''The variables lower_case, upper_case, digits_pass, and symbols_pass are assigned values from the string module, representing different sets of characters'''

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
digits_pass = string.digits
symbols_pass = string.punctuation

#This line concatenates the lowercase letters, uppercase letters, digits, and symbols into a single string named 'password'.

password=lower_case+upper_case+symbols_pass+digits_pass

#This line randomly selects length number of characters from the combined password string and returns them in a new list, shuffled.

suffled=random.sample(password,lenght)

#This line joins the list of shuffled characters into a single string, forming the final password.

password="".join(suffled) #suffling the digits,alphabets and symbols

#This line Provides the user with the generated password, making it visible for use.

print("your generated password:",password)