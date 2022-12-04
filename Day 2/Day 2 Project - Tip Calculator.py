#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number.  You might have to do some Googling to solve this.

#Write your code below this line

#print("Welcome to the tip calculator.")
#bill = input("What was the total bill? ")
#tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
#people = input("How many people to split the bill? ")

#bill_as_float = float(bill)
#tip_as_int = int(tip)
#people_as_int = int(people)
#total_per_person = float(tpp)

#tpp = (bill_as_float / people_as_int) * tip_as_int

#print(f"Each person should pay: ${ttp} ")

#Correct solution (I was close)

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
