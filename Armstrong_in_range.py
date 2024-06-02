# Find the armstrong no.s in a given range
lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))
for i in range(lower, upper+1):
    temp = i
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + digit**(len(str(i)))
        temp //= 10
    if sum == i:
        print(i, end = " ")