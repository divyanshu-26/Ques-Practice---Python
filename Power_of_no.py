# Power of a number means base^expo
# 2^3 = 2*2*2 = 8

base = int(input("Enter the base number: "))
expo = int(input("Enter the expo number: "))
temp = 1
for i in range(expo):
    temp = temp * base

print(f'{base} to the power {expo} is {temp}')