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

print(pizza_frame)
print()
