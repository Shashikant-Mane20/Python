# If cost price and selling price of an item is input through the keyJoard, write a program to determine
# whether the seller has made profit or incurred loss or no profit no loss. Also determine how much profit he
# made or loss he incurred.

cost_price=float(input("Enter cost price:",))
selling_price=float(input("Enter selling price:"))

#profit=sp-cp
profit=selling_price-cost_price
profit_percentage=(profit/cost_price)*100

#loss=cp-sp
loss=cost_price-selling_price
loss_percentage=(loss/cost_price)*100

if selling_price>cost_price:
    print(profit,"profit is made")
    print("Profit Percentage:",profit_percentage,"%")

elif cost_price>selling_price:
    print(loss,"loss is incurred")
    print("Loss Percentage:",loss_percentage,"%")

else:
    print("No profit no loss")

# # Taking cost price and selling price input from the user
# cost_price = float(input("Enter the cost price: "))
# selling_price = float(input("Enter the selling price: "))
 
# # Calculating profit/loss
# profit = selling_price - cost_price
# profit_percentage = (profit / cost_price) * 100
 
# # Checking profit/loss and providing output
# if profit > 0:
#     print("\nThe seller has made a profit of", profit, "units.")
#     print("Profit percentage:", profit_percentage, "%")
# elif profit < 0: 
#     print("\nThe seller has incurred a loss of", abs(profit), "units.")
#     print("Loss percentage:", abs(profit_percentage), "%")
# else:
#     print("\nIt's neither loss nor profit")