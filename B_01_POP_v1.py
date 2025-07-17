import pandas
import numpy as np
from tabulate import tabulate


def make_statement(statement, decoration):
    """Emphasise headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def instructions():
    make_statement("Instructions", "ℹ️")

    print('''

Welcome to the Pizza Order Program! To place your order, first choose whether you want pickup or delivery. If you 
select pickup, enter your name; if delivery, enter your name, address, and phone number (a delivery fee will be 
added). You may order up to 5 pizzas from a menu of 10 options, including gourmet pizzas, with prices shown. After 
selecting your pizzas, To stopped being asked what type of Pizza you want use the exit code "xxx". you can choose 
extra toppings for each one, which also have their own prices. Once you finish ordering, an itemised list of pizzas 
and extras with individual prices will be displayed, along with the total cost, including any delivery charge. If 
your order is for pickup, your name and phone number will be shown; if for delivery, your name, address, 
and phone number will be shown. Your name will be saved with a capital letter at the start and a full stop at the 
end. You can then confirm or cancel your order, and choose to start another order or exit the program.



    ''')


def yes_no(question):
    """Checks that users enter yes/ y or n / no to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n). \n")


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry, this can't be blank. Please try again. \n")


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """Check that users enter the full word
    or the "n" letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


def num_check(question, low, high):
    """ Checks that response is between a low and high boundary number"""

    error = f"Please enter a number between {low} and {high}"

    while True:

        try:
            # check the input is between the correct range
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def currency(y):
    """formats numbers as currency ($##>##)"""
    return "${:.2f}".format(y)


# Variables

# lists to hold pizza details


all_pizza_selected = []
all_pizza_selected_cost = []

selected_pizza_dict = {
    'Pizzas': all_pizza_selected,
    'Prices ($)': all_pizza_selected_cost
}

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

# Main routine goes here

# Main heading
# assume we have no fixed expenses for now
fixed_subtotal = 0
fixed_panda_string = ""

heading = make_statement("Pizza Ordering Program", "🍕")
print(heading)
print()
# Ask user to see instructions
want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

# Ask for their name/ number

# Ask for the number of pizzas
number_of_pizzas = num_check("How many pizzas are you ordering? ", 1, 5)
print()

# Display menu

print(make_statement("Menu", "-"))
print()
print(pizza_frame)

# Ask user to select their pizza

for x in range(number_of_pizzas):
    print()
    pizza_selected = num_check("Enter your choice: ", 1, 10)

    pizza_selected_name = all_pizzas[pizza_selected - 1]
    pizza_selected_cost = all_prices[pizza_selected - 1]

    print(f'You have selected {pizza_selected_name} ${pizza_selected_cost}')

    all_pizza_selected.append(pizza_selected_name)
    all_pizza_selected_cost.append(pizza_selected_cost)

    # ask user if they want extra toppings

    extras = yes_no("Would you like any extras? ")

    if extras == "yes" or extras == "Y":
        print(make_statement("Extras", "-"))
        print()
        print(pizza_frame)

# Display order details
# create dataframe / table from dictionary
selected_pizza_frame = pandas.DataFrame(selected_pizza_dict)

# Rearranging index
selected_pizza_frame.index = np.arange(1, len(selected_pizza_frame) + 1)
print()
print(selected_pizza_frame)

print("The program has ended")
