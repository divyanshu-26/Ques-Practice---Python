# Reverse of a no.
num = int(input("Enter a no.: "))
temp = num
rev = 0
while num != 0:
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10

print("Reverse of the no. is: ", rev)