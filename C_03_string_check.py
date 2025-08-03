#  Functions go here
def string_check(question, valid_ans_list, num_letters):
    """Check that users enter the full word
    or the "n" letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


# Main routine goes here

collection_list = ['pickup', 'delivery']


collection_method = string_check("Pickup or delivery?: ", collection_list, 2)
print(f"You chose {collection_method}")
