# Create a program that do the same functionality without using rstrip() function.
# input string
# remove spaces at the end of the string
# print string

def remove_trailing_space(string):
    for i in range(len(string) - 1, -1, -1):
        if string[i] != " ":
            return string[:i + 1]
    return ""

user_input_string = input("Enter string: ")
no_trailing_space = remove_trailing_space(user_input_string)
print(f'Result: "{no_trailing_space}"')