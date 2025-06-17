# function goes here
def int_check(low, high, question):
    """Checks users enter an integer between two values"""

    error = f"oops - please enter an integer between {low} and {high}."

    while True:

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine goes here

# loop for testing purposes
while True:
    print()

    # ask user for an integer
    my_num = int_check(1, 10, "Choose a number: ")
    print(f"You chose {my_num}")
