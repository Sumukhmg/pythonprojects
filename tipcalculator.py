#Welcome message
print("Welcome to the Tip Calculator.")
#Gather inputs from the user
bill = float(input("What was the total bill? ₹"))
tip_percent = int(input("What percentage tip would you like to give?  "))
people = int(input("How many people to split the bill? "))
#Calculate payment per person and use "{:.2f}".format() to round at 2 decimal places
payment = "{:.2f}".format((bill * (1 + tip_percent / 100)) / people)
#Print amount to pay per person
print("Each person should pay ₹",payment)