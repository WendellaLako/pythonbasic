#Price of house = 300000
#If a buyer has good credit = 10% downpayment
#Otherwise = 28% downpayment

price = 300000
good_credit = False
if good_credit:
    down = 0.1 * price
else:
    down = 0.28 * price

print(f"Payment is RM{down}")