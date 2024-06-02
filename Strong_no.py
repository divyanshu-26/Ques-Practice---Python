# Strong number is a number whose sum of factorial of digits is same as the number.
# For example, 145 is a strong number because 1! + 4! + 5! = 145
num = int(input("Enter a num: "))
def fact(i):
    if i == 0:
        return 1
    else:
        return i * fact(i-1)

sum = 0
for i in str(num):
    sum += fact(int(i))
if sum == num:
    print("Strong number")
else:
    print("Not a strong number")