# Perfect no. is a positive number which is equal to the sum of all its divisors excluding itself.
# For example, 6 is a perfect no. because 1+2+3=6
num = int(input("Enter a num: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print("Perfect no.")
else:
    print("Not a perfect no.")