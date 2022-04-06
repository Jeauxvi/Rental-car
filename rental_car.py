import sys
'''
'''

##start with rentalCode and rentalPeriod(s)##
rentalCode =  input("(B)udget, (D)aily, or (W)eekly rental?\n") 

rentalPeriod = input("Number of Days Rented:\n")

rentalPeriod = input("Number of Weeks Rented:\n")
##start matching the expected output by adding print functions##
print('Rental' ' Summary')
print(rentalCode)
print(rentalPeriod)
##incorporate charges
budget_charge = 40.00
daily_charge = 60.00
weekly_charge = 190.00
##calulate baseCharge
if rentalCode == 'B':
  baseCharge = rentalPeriod * budget_charge
  rentalPeriod = int(rentalPeriod)
  print(baseCharge)
elif rentalCode == 'D':
  rentalPeriod = int(rentalPeriod)
  baseCharge = rentalPeriod * daily_charge

else:
  baseCharge = rentalPeriod * weekly_charge
  rentalPeriod = int(rentalPeriod)

#input mileage variables 
odoStart = input("Starting Odometer Reading:\n")

odoEnd = input("Ending Odometer Reading:\n")
#calculate totalMiles. convert strings to intergers.
totalMiles = int(odoEnd) - int(odoStart)

#calculate mileCharge 
mileCharge = totalMiles * .25

#calculate averageDayMiles. convert intergers to floats.
averageDayMiles = float(totalMiles)/float(rentalPeriod)
#if/ elif functions to calculate extraMiles
if averageDayMiles <= 100:
  extraMiles = 0
elif averageDayMiles > 100:
  extraMiles = averageDayMiles - 100
  extraMiles * .25


#if/else functions to calculate mileCharge
if averageWeekMiles >= 900:
  mileCharge = rentalPeriod * 100.00
else:
  mileCharge = 0.00

# format and calculate amtDue ("%.2f" % amtDue)

amtDue = extraMiles + mileCharge + baseCharge
