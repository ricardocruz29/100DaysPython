#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")
bill = float(input("What awas the total bill? $"))
tip = int(input("What percentage tip would oy uliek to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))


#total_bill = 150 * 1.12 -> 1.12 because when we want the bill corresponding to the percentage
#we would do 150 * 0.12 that equals to x, and then the total bill would be 150 + x, so if we do 
#150*1.12 we are already doing it all
each_person_bill = "{:.2f}".format((bill / number_of_people) * (1+tip/100))

print(f"Each person should pay: ${each_person_bill}")