print("Welcome to the tip calculator.")

# Gathering data
bill_amount = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Processing
total_pay = bill_amount + bill_amount*(tip_percentage/100)
pay_per_person = total_pay/people
pay_per_person = "{:.2f}".format(pay_per_person)

# Output
print(f"Each person should pay: {pay_per_person}")


