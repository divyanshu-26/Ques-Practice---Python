# Find prime no.s in the given range of no.s
lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))
for i in range(lower, upper):
    for j in range(2, i//2):
        if i % j == 0:
            break
    else: print(i, end=" ")
