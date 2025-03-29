# Create a program that do the same functionality without using removesuffix() function.
# ask user input
# remove suffix 
# return remaining string characters
# print string

def remove_suffix(string, suffix):
    if string.endswith(suffix):
        return string[:-len(suffix)]
    return string

user_input_string = input("Enter string: ")
suffix_to_remove = input("Enter suffix to remove: ")
no_suffix = remove_suffix(user_input_string, suffix_to_remove)
print(f'Result: "{no_suffix}"')