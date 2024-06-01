#  Prime number is a no which can be divided by 1 and itself only.
num = int(input("Enter a no.: "))
a = 0
count = 0 
a = num // 2
for i in range(2, a+1):
    if (num % i == 0):
        print(num, "is not a prime no.")
        count = 1
        break

if count == 0:
    print(num, "is a prime no.")