print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill?: $"))
people = int(input("How many people to split the bill?: "))
tip = int(input("What percentage tip would you like to give? 10, 15, or 20?: "))
per_person_bill = float(total_bill/people)
total_per_person = round(per_person_bill * (1+(tip/100)), 2)
print(f"Each person should pay: ${total_per_person}")