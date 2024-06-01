# Armstrong no. Num = sum of digits ^ no of digits
# 153 == 1^3 + 5^3 + 3^3
# 1634 == 1^4 + 6^4 + 3^4 + 4^4
num = int(input("Enter a number: "))
temp = num
sum = 0
while num>0:
    rem = num%10
    sum = sum + rem**len(str(temp))
    num //= 10
if sum == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")