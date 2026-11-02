def is_pangram(sentence):
    lowercase_sentence = sentence.lower()
    letters = set(letter for letter in lowercase_sentence if letter.isalpha())
    return len(letters) == 26