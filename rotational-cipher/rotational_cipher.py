def rotate(text, key):
    rotated_text = ""
    
    for letter in text:
        if not letter.isalpha():
            rotated_text += letter
            
        elif letter.isupper():
            index = ord(letter) - 65
            new_index = (index + key) % 26
            new_letter = chr(new_index + 65)
            rotated_text += new_letter
            
        elif letter.islower():
            index = ord(letter) - 97
            new_index = (index + key) % 26
            new_letter = chr(new_index + 97)
            rotated_text += new_letter

    return rotated_text