# Generates heading (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("instructions", "-")

    print('''
To use this program, simply enter a number more than 0 (excluding 0).
The program will then ask you to enter the unit you convert from and what you want to convert it to.
Please enter suitable units, as it wouldn't be able to convert time to mass, distance to time, or distance to mass.
Time units include ms, sec, min, hr, days, weeks, months, and years.
Distance units include mm, cm, m, ams km.
Mass units include mg, g, kg, and t.

To exit the program, please type 'xxx'.
    ''')


# Main routine goes here

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()

print("program continues")


# Ask user for a number and loop until they
# enter a number that is more than 0 (excluding 0)
def num_check(question):
    error = "Please enter a number that is more than 0\n"
    while True:
        response = input(question).lower()
        if response == "xxx":
            return "xxx"

        try:
            # ask the user for a number
            response = float(response)

            # check that the number is more than 0 (excluding 0)
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here

time_dict = {
    "ms": 86400000,
    "sec": 86400,
    "min": 1440,
    "hr": 24,
    "days": 1,
    "weeks": .142857,
    "months": .0328767,
    "years": .00273973
}

distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": .001
}

mass_dict = {
    "mg": 1000000,
    "g": 1000,
    "kg": 1,
    "t": .001
}

time_units = ['ms', 'sec', 'min', 'hr', 'days', 'weeks', 'months', 'years']
mass_units = ['mg', 'g', 'kg', 't']
distance_units = ['mm', 'cm', 'm', 'km']

while True:

    # Get amount and units
    amount = num_check("Amount? (or 'xxx' to exit) ")

    # exit if user enters exit code...
    if amount == "xxx":
        break

    from_unit = input("From Unit? ")
    to_unit = input("To Unit? ")

    # work out which dictionary to use...
    if from_unit in time_units and to_unit in time_units:
        dict_to_use = time_dict

    elif from_unit in mass_units and to_unit in mass_units:
        dict_to_use = mass_dict

    elif from_unit in distance_units and to_unit in distance_units:
        dict_to_use = distance_dict

    else:
        print("Houston we have mismatched units, please try again")
        continue

    # Multiply to get to our standard value
    multiply_by = dict_to_use[to_unit]
    standard = amount * multiply_by

    # Divide to get to our desired value
    divide_by = dict_to_use[from_unit]
    answer = standard / divide_by

    print(f"There are {answer} {to_unit} in {amount} {from_unit}")
