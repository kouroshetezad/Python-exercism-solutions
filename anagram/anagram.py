def find_anagrams(word, candidates):
    word_lower = word.lower()
    sorted_word = "".join(sorted(word_lower))

    anagrams = []
    
    for candidate in candidates:
        candidate_lower = candidate.lower()
        sorted_candidate = "".join(sorted(candidate_lower))

        if sorted_candidate == sorted_word and candidate_lower != word_lower:
            anagrams.append(candidate)

    return anagrams