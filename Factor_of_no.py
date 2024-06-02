# The factor of a number is a real number which divides the original number completely with zero remainder.
# 16 = 1, 2, 4, 8, 16
# 15 = 1, 3, 5, 15

num = int(input("Enter a number: "))
for i in range(1, num+1):
    if num % i == 0:
        print(i, end=" ")