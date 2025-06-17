import pandas
import numpy as np
# lists to hold pizza details
all_pizzas = ["Cheese", "Pepperoni", "Margherita", "Meat Lovers", "BBQ Beef & Onion",
              "Vegetarian", "Hawaiian", "Ham & Cheese", "Garlic Shrimp", "Chicken Cranberry"]
all_prices = [7.50, 7.50, 10.50, 8.50, 7.50, 7.50, 7.50, 7.50, 10.50, 10.50]

pizza_dict = {
    'Pizzas': all_pizzas,
    'Prices ($)': all_prices,
}

# create dataframe / table from dictionary
pizza_frame = pandas.DataFrame(pizza_dict)

# Rearranging index
pizza_frame.index = np.arange(1, len(pizza_frame) + 1)

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
