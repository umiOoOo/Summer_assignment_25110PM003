# Q93: Write a program to Check string rotation.

str1 = input("Enter the original string: ")
str2 = input("Enter the string to check: ")

# Check if lengths match and if str2 is inside (str1 + str1)
if len(str1) == len(str2) and str2 in (str1 + str1):
    print(f"'{str2}' is a rotation of '{str1}'.")
else:
    print(f"'{str2}' is NOT a rotation of '{str1}'.")