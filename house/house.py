def recite(start_verse, end_verse):
    subjects = [
    "house", "malt", "rat", "cat", "dog", 
    "cow with the crumpled horn", "maiden all forlorn", 
    "man all tattered and torn", "priest all shaven and shorn", 
    "rooster that crowed in the morn", "farmer sowing his corn", 
    "horse and the hound and the horn"
    ]

    verbs = [
    "that Jack built.", "that lay in", "that ate", "that killed", 
    "that worried", "that tossed", "that milked", "that kissed", 
    "that married", "that woke", "that kept", "that belonged to"
    ]
    result = [] 
    for v in range(start_verse, end_verse + 1):
    
        parts = [] 
        for i in range(v - 1, -1, -1):
            phrase = f"the {subjects[i]} {verbs[i]}"
            parts.append(phrase)
        
        full_verse = "This is " + " ".join(parts)
        
        result.append(full_verse)

    return result





















    
    '''output = ""
    index = end_verse - 1
    first_part = f"this is the "
    output = ""
    for i in range(end_verse):
        second_part = f"{subjects[index]} "
        third_part = f"{verbs[index]} "
        output += second_part + third_part
        index -= 1

    final_output = first_part + output
    
    return final_output'''