# Sum of no.s in a given range
lower = int(input("Enter the lower value: "))
upper = int(input("Enter the upper value: "))
sum = 0
for i in range(lower, upper+1):
    sum += i
print(f'Sum of no.s between {lower} and {upper} inclusive is {sum}')