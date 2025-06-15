# Function go here
def make_statement(statement, decoration):
    """Emphasise headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


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


def instructions():
    make_statement("Instructions", "ℹ️")

    print('''

Welcome to the Pizza Order Program! To place your order, first choose whether you want pickup or delivery.
If you select pickup, enter your name; if delivery, enter your name, address, and phone number (a delivery fee will be added).
You may order up to 5 pizzas from a menu of 10 options, including gourmet pizzas, with prices shown.
After selecting your pizzas, you can choose extra toppings for each one, which also have their own prices.
Once you finish ordering, an itemised list of pizzas and extras with individual prices will be displayed, along with the total cost, including any delivery charge.
If your order is for pickup, your name and phone number will be shown; if for delivery, your name, address, and phone number will be shown.
Your name will be saved with a capital letter at the start and a full stop at the end. 
You can then confirm or cancel your order, and choose to start another order or exit the program.



    ''')


# main routine goes here

make_statement("Pizza Ordering Program", "🍕")

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()
print("program continues...")
