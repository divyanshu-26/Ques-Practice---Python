# A number n is said to be Abundant Number to follow these condition
# ● the sum of its proper divisors is greater than the number itself.
# ● And the difference between these two values is called the abundance.

num = int(input("Enter a num: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i

if sum > num:
    print("Abundant Number")
else:
    print("Not Abundant Number")