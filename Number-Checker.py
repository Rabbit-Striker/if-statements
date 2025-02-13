# Print a welcome message
print("Hello, we are here to help you know if the entered number is odd or even")

# Prompt the user to enter a number
num = float(input("Enter a number: "))

# Check if the entered number is a whole number
if num != int(num):
    print("please enter a whole number")
else:
    num = int(num)
    # Check if the number is even
    if num / 2 == int(num / 2):
        print("The number is even")
    else:
        # If the number is not even, it is odd
        print("The number is odd")