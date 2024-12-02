# Even or Odd
# Receive a string form the end user
even_odd_number = input("Please provide a number: ")

# Determines if the string is even or odd
if int(even_odd_number) % 2 == 0:
    print('Even')
else:
    print('Odd')



# Convert a Number to a String!
# Receive a number form the end user
number_to_be_converted = int(input("Please provide a number: "))

# Converts the number to a string
converted_number = str(number_to_be_converted)

# Displays converted number to end user
print(f"Number converted to string: {converted_number}")



# Vowel Count
# Receive a string form the end user
sentence = input("Please provide a sentence you would like to have converted: ")

# Initial variables
vowels = 'aeiou'
vowel_count = 0

# Loops through entire sentence setring to add 1 to the 
# variable counter if it matches an item in the vowel string.
# Converted to lowercase to account for capitalization. 
for item in sentence.lower():
    if item in vowels:
        vowel_count += 1

# Displays total vowels to end user
print(f"There are {vowel_count} vowels in your sentence.")



# Notes: 
# Changed all 'return' to 'print' to make more sense for vscode. 
# Changed all inital variable names to make more sense 
# and gave them inputs instead of default values.
# I made my more comments than nessicary for the sake of the exercize.