# Price of the Item
amount = 1000
Tax = 0.18

# Calculating Total GST for the Item
GST = amount*Tax

print("GST:",+GST)

Total = amount+GST

# If Total Amount is Greater than 1000 apply Discount
if Total > 1000 :
    discount = 0.1
    print("Applying Discount:")
    Dis = Total*discount
    Final_price = Total - Dis
    print("After Apllying Discount: ", +Final_price)
