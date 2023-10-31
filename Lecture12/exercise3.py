import os, shutil
shutil.copy("../Lecture11/remote_exon01.fasta", ".")
sorted(os.listdir())
open('remote_exon01.fasta').read().split()
AJ223353_seq = open('remote_exon01.fasta').read().split()[1]
len(AJ223353_seq)
AJ223353_seq[-3:]
len(AJ223353_seq[0:30])
windowsize = 30
offset = 3
segment_starts = list(range(0,len(AJ223353_seq)-windowsize+1,offset))
segment_starts = list(range(0,len(AJ223353_seq),offset))
segment_starts
basic_fasta_header = '_window' + str(windowsize) + '_offset' + str(offset)
alloutfilename = 'AJ223353_coding_all' + basic_fasta_header + '.fasta'
with open(alloutfilename, 'w') as allsegments :
   allsegments.write('')
   segments_made = []
   fileswanted = 1
   for seg_bits in segment_starts :
    tempseq = AJ223353_seq[seg_bits :seg_bits+windowsize].upper()
    segments_made = segments_made + [tempseq]
# percentage GC content, convert float to integer value
    tempGC = int(100 * (tempseq.count('G') + tempseq.count('C'))/len(tempseq) )
# make a fasta header line
    descriptionline = 'AJ223353_coding_'+str(len(segments_made))+'_'+tempseq+basic_fasta_header
    fastaheader = '>'+descriptionline
    print(len(segments_made),'\t',tempseq,'\t',tempGC)
# Question : do we want files written? Answer will be either True or False ('maybe' is NOT an option!)
    if fileswanted == 1 :
       with open(descriptionline+'.fasta', 'w') as segmentfile :
# output to files
        segmentfile.write(fastaheader+'\n'+tempseq)
        allsegments.write(fastaheader+'\n'+tempseq+'\n\n')
    else:
        allsegments.close()
segmentfile.closed
allsegments.closed
print('\n'.join(segments_made[0:10]))
print(' then '.join(segments_made[0:3]))
for these in 1,2,3 :
    open(alloutfilename).read().split('>')[these]
print('\n'.join(open(alloutfilename).read().split('\n\n')[0:3]))
my_file = open(alloutfilename)
for line in my_file :
    print(line.rstrip('\n\n'))
dir()
os.getcwd()
del os
#os.getcwd()
'os' in dir()
import os
os.getcwd()
len(os.listdir())
os.listdir()
os.listdir()[0]
os.listdir()[1]
#os.listdir('*.dna')
import glob
glob.glob('*.dna')
len(glob.glob('*.dna'))
glob.glob('*.txt')