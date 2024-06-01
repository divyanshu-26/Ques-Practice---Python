# Palindrome no. is a number that gives the same no when reversed.
num = int(input("Enter a no: "))
temp = num
rev = 0
while num>0:
    rem = num%10
    rev = rev*10 + rem
    num //= 10

if temp == rev:
    print(temp, "is a Palindrome no.")
else:
    print(temp, "is not a Palindrome no.")