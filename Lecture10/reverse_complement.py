#!/usr/bin/python
def reverse_complement ():
    """ Computes the reverse complement of the DNA sequence. """
    '''assert validate_dna (dna_seq) "Invalid DNA sequence"'''
    dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

    comp = ""
    for c in dna_seq.upper():
        if c == 'A':
            comp = comp + "T"
        elif c == "T":
            comp = comp + "A"
        elif c == "G":
            comp = comp + "C"
        elif c== "C":
            comp = comp + "G"
    print('the short DNA sequence:', dna_seq)
    print('the complement of this sequence:', comp)

reverse_complement()
