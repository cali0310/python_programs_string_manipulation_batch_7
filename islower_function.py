# create a program that does the same functionality without using islower() function.
# ask user for input
# check if all characters are lowercase
# print result
def is_lower(string):
    for char in string:
        if 'A' <= char <= 'Z':  
            return False
    return True  

user_input_string = input("Enter string: ")
result = is_lower(user_input_string)
print('Result:' ,result)