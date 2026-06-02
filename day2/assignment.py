# Q5: Write a program to Find sum of digits of a number.

num = int(input("Enter a number: "))

digit_sum = 0
temp = num  

while temp > 0:
    last_digit = temp % 10     
    digit_sum = digit_sum + last_digit  
    temp = temp // 10          

print("The sum of digits is:", digit_sum)




# Q6: Write a program to Reverse a number.

num = int(input("Enter a number: "))

reversed_num = 0
temp = num

while temp > 0:
    last_digit = temp % 10
    reversed_num = (reversed_num * 10) + last_digit  
    temp = temp // 10

print("The reversed number is:", reversed_num)



# Q7: Write a program to Find product of digits.

num = int(input("Enter a number: "))

product = 1
temp = num

while temp > 0:
    last_digit = temp % 10
    product = product * last_digit  
    temp = temp // 10

print("The product of digits is:", product)



# Q8: Write a program to Check whether a number is palindrome.

num = int(input("Enter a number: "))

original_num = num  
reversed_num = 0
temp = num

while temp > 0:
    last_digit = temp % 10
    reversed_num = (reversed_num * 10) + last_digit
    temp = temp // 10

if original_num == reversed_num:
    print(original_num, "is a palindrome number.")
else:
    print(original_num, "is not a palindrome number.")
