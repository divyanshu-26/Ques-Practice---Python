# Harshad number is a number that is divisible by the sum of its digits
# Ex - 21 is divisible by (2+1) = 3

num = int(input("Enter a number: "))
temp = num
sum = 0
while num>0:
    digit = num%10
    sum += digit
    num //= 10
if temp % sum == 0:
    print("Harshad no.")
else:
    print("Not a Harshad no.")
    

# In a given range
# lower = int(input("Enter the lower range: "))
# upper = int(input("Enter the upper range: "))
# print("Harshad no.s are: ", end="")
# for i in range(lower, upper):
#     temp = i
#     sum = 0
#     while temp>0:
#         sum += temp%10
#         temp //= 10
#     if i % sum == 0:
#         print(i, end=" ")
    