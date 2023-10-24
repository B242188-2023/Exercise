#!/usr/bin/python
def coding_regions():
    dna_seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

    seq1 = dna_seq[0:62]
    seq2 = dna_seq[90:]

    seq = seq1 + seq2
    print('the coding_regions is:', seq)

    precentage = len(seq)/len(dna_seq)*100
    print('the precentage of coding sequence:', precentage)

    seq1 = seq1.upper()
    seq2 = seq2.upper()
    non_coding = dna_seq[63:89].lower()
    fina = seq1+non_coding+seq2
    print('original genomic DNA sequence:',fina)
coding_regions()
