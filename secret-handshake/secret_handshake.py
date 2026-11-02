def commands(binary_str):
    reversed_binary = binary_str[::-1]
    
    codes = {
        0: 'wink',
        1: 'double blink',
        2: 'close your eyes',
        3: 'jump',
    }
    
    index = 0
    output = []
    
    for binary_digit in reversed_binary[0:4]:
        if int(binary_digit) == 1:
            output.append(codes[index])
        index += 1

    if len(binary_str) == 5 and int(binary_str[0]) == 1:
        output.reverse()
    
    return output
            