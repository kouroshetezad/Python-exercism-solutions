def is_valid(isbn):
    coefficient = 10
    total = 0
    
    isbn = isbn.replace("-","")
    
    if len(isbn) != 10:
        return False
        
    for digit in isbn[:-1]:
        if not digit.isdigit():
            return False

        total += int(digit) * coefficient
        coefficient -= 1

    last_char = isbn[-1]
    if last_char.isdigit():
        total += int(last_char)
    elif last_char == "X":
        total += 10
    else:
        return False
        
    return total % 11 == 0