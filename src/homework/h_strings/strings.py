#HW5

def get_hamming_distance(dna1, dna2):
    
    if len(dna1) != len(dna2):
        return None
    
    distance = 0

    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1

    return distance

def get_dna_complement(dna):
    
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complemented_dna = ''.join(complement_dict.get(char, char) for char in reversed(dna))
    
    return complemented_dna
