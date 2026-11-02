def is_isogram(string):
    lowercase_string = string.lower()
    normalized_sentence = [letter for letter in lowercase_string if letter.isalpha()]
    return len(normalized_sentence) == len(set(normalized_sentence))
