print("Welcome to Cosmic Cinemas!!!")
print("The ticket price is determined based on customer's age, presenting a proof of age is obligatory at entrance. ")

age = int(input("How old are you?: "))

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

print("Thank you for choosing us.")