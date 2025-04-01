# create a program that does the same functionality without using count() function.
# ask user for input
# loop through the string and count occurrences of the substring
# print the count

def count_occurrences(string, substring):
    count = 0
    sub_len = len(substring)
    for i in range(len(string) - sub_len + 1):  
        if string[i:i + sub_len] == substring:  
            count += 1
    return count

user_input_string = input("Enter string: ")
substring_to_count = input("Enter substring to count: ")
result = count_occurrences(user_input_string, substring_to_count)
print('Result:', result)