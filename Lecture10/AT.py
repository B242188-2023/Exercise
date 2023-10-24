#!/usr/bin/python
def at_content_subseq():

    dna_seq = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
    """ 计算DNA序列中的AT含量"""
    a_count = 0
    t_count = 0
    for s in dna_seq:
        if s in "Aa":
            a_count += 1
        elif s in "Tt":
            t_count +=1
    print("the number of A nucleotides:",a_count)
    print("the number of T nucleotides:",t_count)
    print("precentage of AT:",'%.2f' % ((a_count+t_count) / len (dna_seq)))
at_content_subseq()
