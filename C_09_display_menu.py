import pandas

# lists to hold ticket details
all_pizzas = ["A", "B", "C", "D", "E"]
all_prices = [7.50, 7.50, 10.50, 10.50, 6.50]
all_surcharges = [0, 0, 5.53, 5.53, 0]

pizza_dict = {
    'Pizzas': all_pizzas,
    'Prices': all_prices,
    'Surcharge': all_surcharges
}

# create dataframe / table from dictionary
pizza_frame = pandas.DataFrame(pizza_dict)

# Calculate the total payable and profit for each ticket
# pizza_frame['Total'] = pizza_frame['Ticket Price'] + pizza_frame['Surcharge']
# pizza_frame['Profit'] = pizza_frame['Ticket Price'] - 5

# Work out total paid and total profit
# total_paid = pizza_frame['Total'].sum()
# total_profit = pizza_frame['Profit'].sum()

print(pizza_frame)
print()
# print(f"Total Paid: ${total_paid:.2f}")
# print(f"Total Profit: ${total_profit:.2f}")
