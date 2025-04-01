# create a program that does the same functionality without using index() function.
# ask user for input
# loop through the string to find the first occurrence of the substring
# print the index or an error message if not found

def find_index(text, search_term):
    for position in range(len(text) - len(search_term) + 1):
        if text[position : position + len(search_term)] == search_term:
            return position
    raise ValueError("Substring not found")

user_text = input("Enter string: ")
search_text = input("Enter substring to find: ")

try:
    print(f'Result: "{find_index(user_text, search_text)}"')
except ValueError as error:
    print(f'Error: {error}')