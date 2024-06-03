# An automorphic number is a number whose square ends with the same digits as number itself
# ex - 5 = 5^2 = 25
# 25 = 25^2 = 625
num = int(input("Enter a num: "))
sq = num**2
if str(sq).endswith(str(num)):
    print("Automorphic number")
else:
    print("Not an automorphic number")
    
# Find automorphic no.s in a given range
# lower = int(input("Enter the lower range: "))
# upper = int(input("Enter the upper range: "))
# print("Automorphic no.s are: ", end="")
# for i in range(lower, upper):
#     if str(i**2).endswith(str(i)):
#         print(i, end=" ")