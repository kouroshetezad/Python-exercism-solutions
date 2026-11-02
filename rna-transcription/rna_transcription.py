def to_rna(dna_strand):
    rna_strand = ""
    if not dna_strand:
            return ""
    transcription = {
        "G": "C",
        "C": "G",
        "A": "U",
        "T" : "A"
    }
    for letter in dna_strand:
        rna_strand += transcription[letter]
    return rna_strand