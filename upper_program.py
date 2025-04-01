# Create a program that do the same functionality without using upper() function.
# ask user input
# convert to upper without upper() function
# print string

user_input_string = str(input("Enter string: ")).lower()
upper_string = user_input_string.swapcase()
print(upper_string)