mass_dict = {
    "mg": 1000000,
    "g": 1000,
    "kg": 1,
    "t": .001
}

# Get amount and units (assume they are valid)
amount = float(input("Amount? "))
from_unit = input("From Unit? ")
to_unit = input("To Unit? ")

# Multiply to get to our standard value
multiply_by = mass_dict[to_unit]
standard = amount * multiply_by

# Divide to get to our desired value
divide_by = mass_dict[from_unit]
answer = standard / divide_by

print(f"There are {answer:.2f} {to_unit} in {amount} {from_unit}")
