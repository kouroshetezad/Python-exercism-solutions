def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    index = 0
    hamming_distnace = 0
    for i in range(len(strand_a)):
        if strand_a[index] != strand_b[index]:
            hamming_distnace += 1
        index += 1

    return hamming_distnace