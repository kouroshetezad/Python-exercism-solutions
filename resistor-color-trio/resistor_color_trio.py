def label(colors):
    colors_encoded = {
    'black': '0',
    'brown': '1',
    'red': '2',
    'orange': '3',
    'yellow': '4',
    'green': '5',
    'blue': '6',
    'violet': '7',
    'grey': '8',
    'white': '9'
    }
    
    resistance = int(colors_encoded[colors[0]] + colors_encoded[colors[1]]) * (10 ** int(colors_encoded[colors[2]]))
    
    prefixes = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    index = 0
    
    while resistance % 1000 == 0 and resistance >= 1000:
        resistance //= 1000 
        index += 1

    return str(resistance) + " " + prefixes[index]
   