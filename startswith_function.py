# create a program that does the same functionality without using startswith() function.
# ask user for input
# check if the string starts with the given prefix
# print result

def starts_with(string, prefix):
    if len(prefix) > len(string):
        return False
    for i in range(len(prefix)):
        if string[i] != prefix[i]:
            return False
    return True

user_input_string = input("Enter string: ")
prefix_to_check = input("Enter prefix to check: ")
result = starts_with(user_input_string, prefix_to_check)
print('Result:', result)