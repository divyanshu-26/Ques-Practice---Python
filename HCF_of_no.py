# The HCF or the Highest Common Factor of two numbers is the largest common factor of two or more values.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter Second Number:"))
arr = []
if num1 > num2:
    smaller = num2
else:
    smaller = num1
for i in range(1,smaller+1):
    if (num1 % i == 0) and (num2 % i == 0):
        arr.append(i)
print("The HCF of given numbers: {}".format(max(arr)))
