#Create a program using math and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# 1 year = 365 days, 52 weeks, and 12 months

#Don't change the code below
age = input("What is your current age? ")
#Don't change the code above

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

