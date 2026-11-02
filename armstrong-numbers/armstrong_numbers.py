def is_armstrong_number(number):
    if number < 0:
        return False

    numbers_list = [int(num) for num in str(number)]
    
    sum_of_powered_digits = 0
    for digit in numbers_list:
        digit = digit ** len(numbers_list)
        sum_of_powered_digits += digit

    if number == sum_of_powered_digits:
        return True
    else: 
        return False
