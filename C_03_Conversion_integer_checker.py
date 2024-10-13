# Ask user for a number and loop until they
# enter a number that is more than 0 (excluding 0)
def num_check(question):
    error = "Please enter a number that is more than 0\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for a number
            response = float(response)

            # check that the number is more than 0 (excluding 0)
            if 0 < response:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here
while True:
    amount = num_check("Amount: ")
    print("You choose", amount)

    if amount == "xxx":
        break
