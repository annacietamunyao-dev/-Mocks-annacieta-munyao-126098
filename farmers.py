# prompt the farmer for details
cows=int(input("enter number of cows:"))
milk_per_cow=float(input("enter milk produced per cow per day in litres:"))
cost_per_litre=float(input("enter cost per litre of milk:"))
# calculation of total amout of milk and total cost of milk produced 
total_amount=cows*milk_per_cow
total_cost=total_amount*cost_per_litre
# display the results
print("total_amount:",total_amount)
print("total_cost:",total_cost)