# Two numbers are said to be friendly pairs if they have a common abundancy index, the ratio between the sum of divisors of a number and the number itself. These numbers are also known as Amicable numbers. 
# We can also say that two numbers n and m are friendly numbers if
# (n)/n = (m)/m
# Where (n) is the sum of divisors of n.

num1 = int(input("Enter the first no.: "))
num2 = int(input("Enter the second no.: "))
sum1, sum2 = 0, 0
for i in range(1, num1):
    if num1 % i == 0:
        sum1 += i
for i in range(1, num2):
    if num2 % i == 0:
        sum2 += i

if (sum1/num1) == (sum2/num2):
    print(f'{num1} and {num2} is a friendly pair')
else:
    print(f'{num1} and {num2} is not a friendly pair')