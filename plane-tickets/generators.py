"""Functions to automate Conda airlines ticketing system."""

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    letters = ["A", "B", "C", "D"]
    for i in range(number):
        yield letters[i % 4]

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    letters = ['A', 'B', 'C', 'D']
    row = 1
    count = 0

    while count < number:
        if row == 13:
            row += 1
        for letter in letters:
            if count >= number:
                break
            yield f"{row}{letter}"
            count += 1
        row += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seat_assignment = {}
    seat_letters = ["A", "B", "C", "D"]
    seat_row = 1

    seat_letter_index = 0

    for passenger in passengers:
        seat_number = str(seat_row) + seat_letters[seat_letter_index]

        seat_assignment[passenger] = seat_number

        seat_letter_index += 1
        if seat_letter_index >= len(seat_letters):
            seat_letter_index = 0
            seat_row += 1

    return seat_assignment

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers (e.g., '1A', '24B').
    :param flight_id: str - string containing the flight identifier (e.g., 'LH778').
    :return: generator - generator that yields 12-character long ticket codes.
    """

    for seat in seat_numbers:

        base_code = seat + flight_id

        current_length = len(base_code)

        padding_needed = 12 - current_length
        if padding_needed > 0:
            zero_padding = "0" * padding_needed
        else:

            zero_padding = ""
        ticket_code = base_code + zero_padding
        final_ticket_code = ticket_code[:12]
        yield final_ticket_code
