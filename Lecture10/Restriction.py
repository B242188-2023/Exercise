#!/usr/bin/python
def restriction ():
    dna_seq = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'
    motif_position = dna_seq.find('GAATTC')

    i = 0
    fragment1 = ''
    fragment2 = ''
    while i < len(dna_seq):
        if i <= motif_position:
            fragment1 = fragment1 + dna_seq[i]
            i += 1
        else:
            fragment2 = fragment2 + dna_seq[i]
            i += 1
    print('the motif_position start from:', motif_position)
    print('the first fragment length is:', len(fragment1))
    print('the second fragment length is:', len(fragment2))

restriction()
