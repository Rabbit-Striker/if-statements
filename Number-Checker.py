
print("Hello, we are here to help you know if the entered number is odd or even")
num = float(input("Enter a number: "))
if num != int(num):
    print("please enter a whole number")
else:
    num = int(num)
    if num/2 == int(num/2):
        print("The number is even")
    else:
        print("The number is odd")