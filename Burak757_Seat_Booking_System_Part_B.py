import random
import string

# Seat-Booking Application for Burak757

# Initialize the seat status
seats = [['F'] * 80 for _ in range(6)]     # Create a 6x80 matrix with all seats initially set as 'F' (Free).
seats[3][76:78] = ['S'] * 2                 # Designate seats 77D, 78D as storage areas.
seats[4][76:78] = ['S'] * 2                 # Designate seats 77E, 78E as storage areas.
seats[5][76:78] = ['S'] * 2                 # Designate seats 77F, 78F as storage areas.80

# Database to store booking details
database = {}


# Function to generate a random booking reference
def generate_booking_reference():
    while True:
        # Generate a random string of uppercase letters and digits, with a length of 8.
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        # Check if the generated reference is not already present in the database.
        if reference not in database:
            return reference    # If the reference is unique, return it as the generated booking reference.


def check_seat_availability():
    """
    Function to check the availability of a seat.
    """
    seat_number = input("Enter the seat number (e.g., 1A): ")    # Prompt the user to enter the seat number.
    column = int(seat_number[:-1]) - 1      # Extract the column number from the seat number.
    row = ord(seat_number[-1]) - ord('A')    # Extract the row number from the seat number.

    if 0 <= row < len(seats) and 0 <= column < len(seats[0]):
        seat_status = seats[row][column]    # Get the status of the seat from the seats matrix.
        if seat_status == 'F':
            print(f"Seat {seat_number} is Free.")
        elif seat_status == 'R':
            print(f"Seat {seat_number} is Booked.")
        elif seat_status == 'S':
            print(f"Seat {seat_number} is a Storage Area.")
        else:
            print(f"Seat {seat_number} is Unavailable.")
    else:
        print("Invalid seat number.")

# Function to book a seat
def book_seat():
    seat_number = input("Enter the seat number to book (e.g., 1A): ")    # Prompt the user to enter the seat number to book.
    # Extract the row number from the seat number
    row = ord(seat_number[-1]) - ord('A')
    # Extract the column letter from the seat number
    column = int(seat_number[:-1]) - 1

    if seats[row][column] == 'F':    # If the seat is currently free ('F'), proceed with the booking.
        booking_reference = generate_booking_reference()    # Generate a unique booking reference.
        passport_number = input("Enter passenger's passport number: ")    # Prompt the user to enter the passenger's passport number.
        first_name = input("Enter passenger's first name: ")    # Prompt the user to enter the passenger's first name.
        last_name = input("Enter passenger's last name: ")    # Prompt the user to enter the passenger's last name.

        seats[row][column] = booking_reference    # Update the seat status to the booking reference.
        database[booking_reference] = {    # Add the booking details to the database.
            'passport_number': passport_number,
            'first_name': first_name,
            'last_name': last_name,
            'seat_number': seat_number ,

        }

        print(f"Seat {seat_number} has been booked with reference {booking_reference}.")    # Print a confirmation message.
    elif seats[row][column] == 'S':
        print("Sorry, the seat is a Storage Area and cannot be booked.")
    else:    # If the seat is already booked , display an error message.
        print("Sorry, the seat is already booked.")

# Function to free a seat
def free_seat():
    seat_number = input("Enter the seat number to free (e.g., 1A): ")    # Prompt the user to enter the seat number to free.
    # Extract the row number from the seat number
    row = ord(seat_number[-1]) - ord('A')
    # Extract the column letter from the seat number
    column = int(seat_number[:-1]) - 1
    if seats[row][column] =='S':
        print("the seat cannot be freed because it is storage area")
    elif seats[row][column] != 'F':    # If the seat is currently booked  remove the booking from the database.
        booking_reference = seats[row][column]    # Get the booking reference associated with the seat.
        del database[booking_reference]    # Delete the entry from the database.
        seats[row][column] = 'F'  # Set the seat status to 'F' (free).
        # Print a confirmation message indicating that the seat has been freed.
        print(f"Seat {seat_number} has been freed.")





# Function to show the booking state
def show_booking_state():
    print("Booking State:")    # Print the heading for the booking state.

    for i, row in enumerate(seats):    # Iterate over each row in the seats.
        for j, seat in enumerate(row):    # Iterate over each seat in the current row.
            seat_number = f"{j+1}{chr(i+65)}"    # Generate the seat number based on the row and column indices.
            print(f"{seat_number}:{seat}", end=' ')    # Print the seat number and its status.
        print()    # Move to the next line after printing the seats in the current row.

# Function to print the database storing booking details
def print_booking_database():
    print("\nBooking Database:")    # Print the heading for the booking database.

    for reference, details in database.items():    # Iterate over each item in the database.
        print(f"Reference: {reference}")    # Print the booking reference.
        print(f"Passport Number: {details['passport_number']}")    # Print the passport number associated with the booking.
        print(f"First Name: {details['first_name']}")    # Print the first name of the passenger.
        print(f"Last Name: {details['last_name']}")    # Print the last name of the passenger.
        print(f"Seat: {details['seat_number']}")    # Print the seat row and column for the booking.
        print()    # Print a blank line to separate each booking entry.
# Main program loop
while True:
    print("\nMenu:")    # Print the menu options.
    print("1. Check availability of seat")
    print("2. Book a seat")
    print("3. Free a seat")
    print("4. Show booking state")
    print("5. Show booking references database")
    print("6. Exit program")

    choice = input("Enter your choice (1-5): ")    # Prompt the user to enter their choice.

    if choice == '1':    # If the choice is '1', check the availability of a seat.
        check_seat_availability()
    elif choice == '2':    # If the choice is '2', book a seat.
        book_seat()
    elif choice == '3':    # If the choice is '3', free a seat.
        free_seat()
    elif choice == '4':    # If the choice is '4', show the booking state.
        show_booking_state()
    elif choice == '5':    # If the choice is '5', show the booking references database.
        print_booking_database()
    elif choice == '6':    # If the choice is '6', exit the program.
        print("Exiting program...")
        break
    else:    # If the choice is invalid, print an error message.
        print("Invalid choice. Please try again.")