def get_valid_number(prompt, minimum, maximum):
    while True:
        try:
            value = float(input(prompt))

            if value < minimum or value > maximum:
                print(
                    f"Invalid value! Please enter a number "
                    f"between {minimum} and {maximum}."
                )
            else:
                return value

        except ValueError:
            print("Invalid input! Please enter a number.")