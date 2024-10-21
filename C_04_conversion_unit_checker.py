# Ask user for units
def get_unit():

    while True:
        response = input("Unit: ").lower()

        # check for the exit code
        if response == "xxx":
            return response

        # check if the unit is in milliseconds
        elif response in ['Milliseconds', 'Millisecond', 'milliseconds', 'millisecond', 'ms']:
            return "milliseconds"

        # check if the unit is in seconds
        elif response in ['Seconds', 'Second', 'seconds', 'second', 'sec']:
            return "seconds"

        # check if the unit is in minutes
        elif response in ['Minutes', 'Minute', 'minutes', 'minute', 'min']:
            return "minutes"

        # check if the unit is in hours
        elif response in ['Hours', 'Hour', 'hours', 'hour', 'hr']:
            return "hours"

        # check if the unit it is in days
        elif response in ['Days', 'Day', 'days', 'day']:
            return "days"

        # check if the unit is in weeks
        elif response in ['Weeks', 'Week', 'weeks', 'week']:
            return "weeks"

        # check if the unit is in months
        elif response in ['Months', 'Month', 'months', 'month']:
            return "months"

        # check if the unit is in years
        elif response in ['Years', 'Year', 'years', 'year']:
            return "years"

        # check if the unit is in millimetres
        elif response in ['Millimetres', 'Millimetre', 'Millimeters',
                          'Millimeter', 'millimetres', 'millimetre',
                          'millimeters', 'millimeter', 'mm']:
            return "millimetres"

        # check if the unit is in centimetres
        elif response in ['Centimetres', 'Centimetre', 'centimetres',
                          'centimetre', 'Centimeters', 'Centimeter',
                          'centimeter', 'centimeters', 'cm']:
            return "centimetres"

        # check if the unit is in metres
        elif response in ['Metres', 'Metre', 'metres', 'metre',
                          'Meters', 'Meter', 'meters', 'meter', 'm']:
            return "metres"

        # check if the unit is in kilometres
        elif response in ['Kilometres', 'Kilometre', 'kilometres',
                          'kilometre', 'Kilometers', 'Kilometer',
                          'kilometers', 'kilometer', 'km']:
            return "kilometres"

        # check if the unit is in milligrams
        elif response in ['Milligrams', 'milligrams', 'mg']:
            return "milligrams"

        # check if the unit is in grams
        elif response in ['Grams', 'grams', 'g']:
            return "grams"

        # check if the unit is in kilograms
        elif response in ['Kilograms', 'kilograms', 'kg']:
            return "kilograms"

        # check if the unit is in tonnes
        elif response in ['Tonnes', 'tonnes', 't']:
            return "tonnes"

        # if the response is invalid output an error
        else:
            print("Please enter a valid unit")


# Main routine goes here
while True:
    unit = get_unit()

    print(f"You chose {unit}")

    if unit == "xxx":
        print('Thank you for using the conversion calculator')
        break
