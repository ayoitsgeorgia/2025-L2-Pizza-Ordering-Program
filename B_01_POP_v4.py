import pandas
import numpy as np


def make_statement(statement, decoration):
    """Emphasise headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def instructions():
    make_statement("Instructions", "ℹ️")

    print('''

Welcome to the Pizza Order Program! To place your order, first choose whether you want pickup or delivery delivery will 
cost a fee of $14.50. If you select pickup, enter your name; if delivery, enter your name, address, and phone number 
(a delivery fee will be added). You may order up to 5 pizzas from a menu of 10 options, including gourmet pizzas, 
with prices shown. After selecting your pizzas, To stopped being asked what type of Pizza you want use the exit code
"xxx". you can choose extra toppings for each one, which also have their own prices. Once you finish ordering, 
an itemised list of pizzas and extras with individual prices will be displayed, along with the total cost, including any
delivery charge. If your order is for pickup, your name and phone number will be shown; if for delivery, your name,
address, and phone number will be shown. Your name will be saved with a capital letter at the start and a full stop at
the end. You can then confirm or cancel your order, and choose to start another order or exit the program.



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


def digit_check(question):
    while True:
        user_input = input(question)
        if user_input.isdigit() and len(user_input) == 10:
            try:
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        else:
            print("Invalid input. Please enter a 10-digit phone number.")


def num_check(question, low, high):
    """ Checks that response is between a low and high boundary number"""

    error = f"Please enter a number between {low} and {high} "

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
DELIVERY_CHARGE = 14.50

# lists to hold pizza details
all_pizza_selected = []
all_pizza_selected_cost = []

# lists to hold extras details

all_extras_selected = []
all_extras_selected_cost = []

selected_pizza_dict = {
    'Pizzas': all_pizza_selected,
    'Pizza Prices ($)': all_pizza_selected_cost,
    'Extras': all_extras_selected,
    'Extra Prices ($)': all_extras_selected_cost,
}

all_pizzas = ["Cheese", "Pepperoni", "Margherita", "Meat Lovers", "BBQ Beef & Onion",
              "Vegetarian", "Hawaiian", "Ham & Cheese", "Garlic Shrimp", "Chicken Cranberry"]
all_prices = [7.50, 7.50, 10.50, 8.50, 7.50, 7.50, 7.50, 7.50, 10.50, 10.50]

pizza_dict = {
    'Pizzas': all_pizzas,
    'Prices ($)': all_prices,

}

all_extras = ["Mushroom", "Pepperoni", "Pineapple", "BBQ Sauce", "Mozzarella"]

all_extras_prices = [0.50, 1, 0.50, .50, 1]

extras_dict = {
    'Extras': all_extras,
    'Prices ($)': all_extras_prices,
}

# create dataframe / table from dictionary
pizza_frame = pandas.DataFrame(pizza_dict)

extras_frame = pandas.DataFrame(extras_dict)
# Rearranging index
pizza_frame.index = np.arange(1, len(pizza_frame) + 1)

extras_frame.index = np.arange(1, len(extras_frame) + 1)

while True:
    # Main routine goes here

    # CLEAR THE PREVIOUS ORDERS DATA
    all_pizza_selected_cost.clear()
    all_extras_selected_cost.clear()
    all_extras_selected.clear()
    all_pizza_selected.clear()

    # Main heading
    # assume we have no fixed expenses for now
    fixed_subtotal = 0
    fixed_panda_string = ""

    heading = make_statement("Pizza Ordering Program", "🍕")
    print(heading)
    print()
    # Ask user to see instructions
    want_instructions = yes_no("Would you like to see the instructions? ")

    if want_instructions == "yes":
        instructions()

    print()

    # Ask for the number of pizzas
    number_of_pizzas = num_check("How many pizzas are you ordering? ", 1, 5)
    print()

    # Ask if it's pick up or delivery
    name = not_blank("Enter a name for this order: ")
    print()

    pickup_or_delivery = yes_no("Is this order for pickup? ")
    if pickup_or_delivery == "yes":
        delivery = 'no'
        print("You have selected Pickup")
        print()
        digit_check("Enter a phone number for the order: ")

    else:
        print("You have selected Delivery")
        delivery = 'yes'
        print()
        digit_check("Enter a phone number for the order: ")
        print()
        address = not_blank("Enter the address this order will be delivered to: ")

    # Display menu

    print()
    print(make_statement("Menu", "-"))
    print()
    print(pizza_frame)

    print()
    print(make_statement("Extras", "-"))
    print()
    print(extras_frame)
    print()

    # Ask user to select their pizza

    for x in range(number_of_pizzas):
        print()
        pizza_selected = num_check("Enter your choice of pizzas: ", 1, 10)

        pizza_selected_name = all_pizzas[pizza_selected - 1]
        pizza_selected_cost = all_prices[pizza_selected - 1]

        print(f'You have selected {pizza_selected_name} ${pizza_selected_cost}')

        all_pizza_selected.append(pizza_selected_name)
        all_pizza_selected_cost.append(pizza_selected_cost)

        # ask user if they want extra toppings

        extras = yes_no("Would you like any extras? ")

        if extras == "yes" or extras == "Y":
            print()
            extras_selected = num_check("Enter your choice of extras: ", 1, 5)

            extras_selected_name = all_extras[extras_selected - 1]
            extras_selected_cost = all_extras_prices[extras_selected - 1]

            print(f'You have selected {extras_selected_name} ${extras_selected_cost}')

            all_extras_selected.append(extras_selected_name)
            all_extras_selected_cost.append(extras_selected_cost)

        else:

            all_extras_selected.append("No extras")
            all_extras_selected_cost.append(0.0)

    # how to display table with pizza and extras and combined costs?

    combined_order_total = sum(all_extras_selected_cost) + sum(all_pizza_selected_cost)

    # Display order details
    # create dataframe / table from dictionary
    selected_pizza_frame = pandas.DataFrame(selected_pizza_dict)

    # Rearranging index
    selected_pizza_frame.index = np.arange(1, len(selected_pizza_frame) + 1)
    print()
    print(selected_pizza_frame)
    print(f'Total price: ${combined_order_total}')

    # ask user for payment method (cash / credit / ca / cr)
    payment_ans = ('cash', 'credit')
    # credit card surcharge (currently 10%)
    CREDIT_SURCHARGE = 0.10

    pay_method = string_check("Payment method: ", payment_ans, 2)

    if pay_method == "cash":
        surcharge = 0

    # if paying by credit, calculate surcharge
    else:
        surcharge = round(combined_order_total * CREDIT_SURCHARGE, 2)
        combined_order_total += surcharge

    print(f"The surcharge is ${surcharge}, the total is ${combined_order_total}")

    # Add delivery fee
    if delivery == "yes":
        combined_order_total += DELIVERY_CHARGE
        print(f"The delivery fee is ${DELIVERY_CHARGE}")
        print(f"The overall total is ${combined_order_total}")

    print()
    confirm = yes_no("Would you like to confirm your order? ")
    if confirm == "yes":
        print("Thank you for your order")

    else:
        print("your order has been canceled")

    want_more = yes_no("Would you like to order any more pizzas? ")

    if want_more != "yes":
        print()
        print("The program has ended")
        break  # Exit the loop if the user does not enter yes

