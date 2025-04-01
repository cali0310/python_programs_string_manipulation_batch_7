# create a program that does the same functionality without using rjust() function.
# ask user for input
# calculate the number of spaces needed
# add spaces at the beginning of the string
# print the right-justified string

def right_justify(string, width):
    spaces = max(0, width - len(string))
    return ' ' * spaces + string

user_input_string = input("Enter string: ")
total_width = int(input("Enter total width: "))
result = right_justify(user_input_string, total_width)
print(f'Result: "{result}"')