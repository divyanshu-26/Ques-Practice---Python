# Sum of first N natural no.s (Positive no.s starting from 1)
N = int(input("Enter the value of N: "))
sum = 0
for i in range(1,N+1):
    sum += i
print("The sum of first",N,"natural numbers is:",sum)

# OR sum = (num * (num + 1))/2