#  Functions go here
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


# Main routine goes here
collection_list = ['pickup', 'delivery']

want_instructions = string_check("Do you want to see the instructions? ")
print(f"You chose {want_instructions}")
collection_method = string_check("Pickup or Delivery?: ", collection_list, 2)
print(f"You chose {collection_method}")
