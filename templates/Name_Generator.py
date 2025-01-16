print("Welcome to the pet name generator")
character = input("What is your favorite Movie Character? ")
activity = input("What is your favorite activity? ")
food_brand_name = input("What is your favorite food? ")
# Loop until valid gender input is entered
while True:
    # Get the gender input and convert it to lowercase to make it case-insensitive
    gender = input("Is your Pet male or female? (m/f): ").lower()  # Convert input to lowercase

    if gender == 'm':  # Check if the input is 'm' for male
        print("Your pet name could be Mr. " + character + " " + activity + " " + food_brand_name)
        break  # Exit the loop once a valid input is entered
    elif gender == 'f':  # Check if the input is 'f' for female
        print("Your pet name could be Miss " + character + " " + activity + " " + food_brand_name)
        break  # Exit the loop once a valid input is entered
    else:
        # If the input is invalid, prompt the user again
        print("Invalid input. Please enter 'm' for male or 'f' for female.")
        # The loop will continue here, asking for gender input again
