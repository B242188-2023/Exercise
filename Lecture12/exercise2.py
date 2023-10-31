genomic_dna2 = open('genomic_dna2.txt').read().upper()
len(genomic_dna2)
exons_v1 = open('exons.txt').read().replace(',','\n').split()
exons_v1
exons_v2 = open('exons.txt').read().rstrip()
exons_v2
counter=0
for exons in exons_v2 :
    counter += 1
    print(counter,exons)
exons_v3 = open('exons.txt').read().rsplit()
exons_v3
counter=0
for exons in exons_v3 :
    counter += 1
    print(counter,exons)
counter=0
with open('Exercise2_coding_seqence.fasta','w') as fullcoding :
    fullcoding.write('>Lecture12_exercise2_codingseq\n')
    for exons in exons_v3 :
        counter += 1
        startexon = int(exons.split(',')[0])-1
        endexon = int(exons.split(',')[1])
        exonwanted = genomic_dna2[startexon :endexon]
        fullcoding.write(exonwanted)
        regionsummary = 'Exon'+str(counter)+' '+str(exons)+' runs from index position '+str(startexon)+' upto but not including '+str(endexon)+ '.'
        print(regionsummary,'\n\t',exonwanted)
fullcoding.closed
print(open('Exercise2_coding_seqence.fasta').read())
