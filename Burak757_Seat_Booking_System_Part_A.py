# Seat-Booking Application for Burak757

# Initialize the seat status
seats = [['F'] * 80 for _ in range(6)]     # Create a 6x80 matrix with all seats initially set as 'F' (Free).
seats[3][76:78] = ['S'] * 2                 # Designate seats 77D, 78D as storage areas.
seats[4][76:78] = ['S'] * 2                 # Designate seats 77E, 78E as storage areas.
seats[5][76:78] = ['S'] * 2                 # Designate seats 77F, 78F as storage areas.

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


def book_seat():
    """
    Function to book a seat.
    """
    seat_number = input("Enter the seat number to book (e.g., 1A): ")    # Prompt the user to enter the seat number.
    column = int(seat_number[:-1]) - 1      # Extract the column number from the seat number.
    row = ord(seat_number[-1]) - ord('A')    # Extract the row number from the seat number.

    if seats[row][column] == 'F':
        seats[row][column] = 'R'            # Book the seat by updating its status to 'R'.
        print(f"Seat {seat_number} has been booked.")
    elif seats[row][column] == 'R':
        print("Sorry, the seat is already booked.")
    elif seats[row][column] == 'S':
        print("Sorry, the seat is a Storage Area and cannot be booked.")
    else:
        print("Invalid seat number.")


def free_seat():
    """
    Function to free a seat.
    """
    seat_number = input("Enter the seat number to free (e.g., 1A): ")    # Prompt the user to enter the seat number.
    column = int(seat_number[:-1]) - 1      # Extract the column number from the seat number.
    row = ord(seat_number[-1]) - ord('A')    # Extract the row number from the seat number.

    if seats[row][column] == 'R':
        seats[row][column] = 'F'            # Free the seat by updating its status to 'F'.
        print(f"Seat {seat_number} has been freed.")
    elif seats[row][column] == 'F':
        print("The seat is already available.")
    elif seats[row][column] == 'S':
        print("The seat is a Storage Area and cannot be freed.")
    else:
        print("Invalid seat number.")


def show_booking_state():
    """
    Function to show the booking state.
    """
    print("Booking State:")
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            seat_number = f"{j+1}{chr(i+65)}"    # Generate the seat number based on the row and column indices.
            print(f"{seat_number}:{seat}", end=' ')    # Print the seat number and its status.
        print()


# Main program loop
while True:
    print("\nMenu:")
    print("1. Check availability of seat")
    print("2. Book a seat")
    print("3. Free a seat")
    print("4. Show booking state")
    print("5. Exit program")

    choice = input("Enter your choice (1-5): ")    # Prompt the user to enter a choice.

    if choice == '1':
        check_seat_availability()
    elif choice == '2':
        book_seat()
    elif choice == '3':
        free_seat()
    elif choice == '4':
        show_booking_state()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")