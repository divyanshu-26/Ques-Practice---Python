# Factorial of a number. Factorial is a sequence of a number whose multiply by all previous numbers

num = int(input("Enter a number: "))
fact = 1
for i in range(num, 0, -1):
    fact *= i
print(f'Factorial of {num} is {fact}')

# By recursion
# def factorial(num):
#     fact = 1
#     if num == 0:
#         return fact
#     else:
#         fact = num * factorial(num - 1)
#     return fact

# print(factorial(5))