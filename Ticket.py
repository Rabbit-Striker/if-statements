# Welcome message
print("Welcome to Cosmic Cinemas!!!")

# Information about ticket pricing
print("The ticket price is determined based on customer's age, presenting a proof of age is obligatory at entrance. ")

# Get the age of the customer
age = int(input("How old are you?: "))

# Determine the ticket price based on age
if age >= 40:
    print("Your ticket price is: 10$")
elif age >= 18:
    print("Your ticket price is: 12$")
elif age >= 10:
    print("Your ticket price is: 8$")
elif age >= 4:
    print("Your ticket price is: 5$")
else:
    print("Sorry, by our regulations, children under 4 years are not allowed.")

# Thank you message
print("Thank you for choosing us.")