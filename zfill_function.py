# create a program that does the same functionality without using zfill() function.
# ask user for input
# calculate the number of zeros needed
# add zeros at the beginning of the string
# print the zero-filled string

def zero_fill(string, width):
    zeros = max(0, width - len(string))
    return '0' * zeros + string

user_input_string = input("Enter string: ")
total_width = int(input("Enter total width: "))
result = zero_fill(user_input_string, total_width)
print(f'Result: "{result}"')