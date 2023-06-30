import math

print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")

user_choice = input("Enter either 'Investment' or 'Bond' from the menu above to proceed: ")

# using "lower()" to validate user input
user_choice = user_choice.lower()

# investment calculation
if user_choice.lower() == "investment":
 deposit_amount = float(input("Enter the amount of money you are depositing: "))
 interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
 year_duration = float(input("Enter the number of years you plan on investing: "))
 interest_type = input("Enter either 'Simple' or 'Compound' ")

# calculating for simple interest
 if interest_type.lower() == "simple":
  simp_interest = deposit_amount * (1 + interest_rate * year_duration)
  print("The total amount you will get back is: ", simp_interest)

# calculating for compound interest
 elif interest_type.lower() == "compound":
  comp_interest = deposit_amount * math.pow((1 + interest_rate), year_duration)
  print("The total amount you will get back is: ", comp_interest)

 else:
  print("Invalid interest type, please try again.")
  

# bond calculation
elif user_choice.lower() == "bond":
 present_house_value = float(input("Enter the present value of the house: "))
 interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100 / 12
 month_duration = float(input("Enter the number of months you plan to take to repay the bond: "))

 repayment = (interest_rate * present_house_value) / (1 - math.pow((1 + interest_rate), - month_duration))

 print("The amount you will have to repay each month is: ", repayment)

else:
 print("Invalid choice, please try again.")