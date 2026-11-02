def resistor_label(colors):
    RESISTANCE_VALUES = {
        'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4',
        'green': '5', 'blue': '6', 'violet': '7', 'grey': '8', 'white': '9'
    }
    
    TOLERANCE_VALUES = {
        'grey': '0.05', 'violet': '0.1', 'blue': '0.25', 'green': '0.5',
        'brown': '1', 'red': '2', 'gold': '5', 'silver': '10'
    }

    if len(colors) == 1:
        return "0 ohms"

    tolerance_color = colors[-1]
    multiplier_color = colors[-2]
    digit_colors = colors[:-2]

    value_str = "".join(RESISTANCE_VALUES[color] for color in digit_colors)
    resistance = int(value_str) * (10 ** int(RESISTANCE_VALUES[multiplier_color]))

    prefixes = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    prefix_index = 0
    
    while resistance >= 1000:
        resistance /= 1000
        prefix_index += 1

    return f"{resistance:g} {prefixes[prefix_index]} ±{TOLERANCE_VALUES[tolerance_color]}%"