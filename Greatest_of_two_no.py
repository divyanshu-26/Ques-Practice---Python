# Greatest of two given no.s
def max(a,b):
    if a>b:
        return a
    else:
        return b
num1 = int(input("Enter a no: "))
num2 = int(input("Enter a no: "))
print(max(num1, num2), "is the greater.")