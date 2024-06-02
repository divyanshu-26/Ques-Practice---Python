# Fibonacci Series upto Nth term. The sequence is a Fibonacci series where the next number is the sum of the previous two numbers. The first two terms of the Fibonacci sequence start from 0,1,…
# 0, 1, 1, 2, 3, 5,....

N = int(input("Enter the value of N: "))
a, b = 0, 1
print("Fibonacci Series: ", end =" ")
for i in range(N):
    print(a, end=", ")
    a, b = b, a+b
    