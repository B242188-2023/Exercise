import os, subprocess, shutil
#os.mkdir("../Lecture11")
os.chdir("../Lecture11")
os.listdir()
subprocess.call("cp /localdisk/data/BPSM/Lecture11/plain_genomic_seq.txt . ",shell=True)
os.system("cp /localdisk/data/BPSM/Lecture11/plain_genomic_seq.txt . ")
shutil.copy("/localdisk/data/BPSM/Lecture11/plain_genomic_seq.txt" , "./shutilversion.txt" )
os.listdir()
print("\n".join(os.listdir()))
print(open("plain_genomic_seq.txt").read())
print(open("plain_genomic_seq.txt").read().rstrip())
local_seq = open("plain_genomic_seq.txt").read().rstrip()
local_seq
remotefile = open("AJ223353_noheader.fasta2").read().upper()
remotefile
len(remotefile)
local_seq = open("plain_genomic_seq.txt").read().upper()
local_seq
len(local_seq)
len(local_seq.rstrip())
dir()
remotefile_singleline = remotefile.replace("\n","")
remotefile_singleline
remotefile_singleline_ready = remotefile_singleline
len(remotefile_singleline_ready)
local_seq_singleline = local_seq.replace("\n","")
local_seq_singleline
len(local_seq_singleline)
remotefile_singleline_anythingleft = remotefile_singleline.replace("G","").replace("A","").replace("T","").replace("C","")
remotefile_singleline_anythingleft
local_seq_singleline_anythingleft = local_seq_singleline.replace("G","").replace("A","").replace("T","").replace("C","")
local_seq_singleline_anythingleft
local_seq_singleline_reallyDNA = local_seq_singleline.replace("X","").replace("S","").replace("K","").replace("L","")
local_seq_singleline_reallyDNA
set(list(local_seq.rstrip()))
len(local_seq_singleline_reallyDNA)
len(local_seq_singleline)
local_seq_singleline_ready = local_seq_singleline_reallyDNA
remote_noncoding01 = remotefile_singleline_ready[0:28]
remote_exon01 = remotefile_singleline_ready[28:409]
remote_noncoding02 = remotefile_singleline_ready[409:]
remote_noncoding01
remote_exon01
remote_noncoding02
len(remote_noncoding01) + len(remote_exon01) + len(remote_noncoding02)
local_exon01 = local_seq_singleline_ready[0:63]
local_intron01 = local_seq_singleline_ready[63:90]
local_exon02 = local_seq_singleline_ready[90:]
local_exon01
local_intron01
local_exon02
len(local_exon01)+len(local_intron01)+len(local_exon02)
remote_noncoding01_out = open("remote_noncoding01.fasta", "w")
remote_noncoding01_out.write(">AJ223353_noncoding01_length" + str(len(remote_noncoding01)) + "\n")
remote_noncoding01_out.write(remote_noncoding01)
remote_noncoding01_out.close()
print(open("remote_noncoding01.fasta").read())
remote_exon01_out = open("remote_exon01.fasta", "w")
remote_exon01_out.write(">AJ223353_exon01_length" + str(len(remote_exon01)) + "\n")
remote_exon01_out.write(remote_exon01)
remote_exon01_out.close()
print(open("remote_exon01.fasta").read())
remote_noncoding02_out = open("remote_noncoding02.fasta", "w")
remote_noncoding02_out.write(">AJ223353_noncoding02_length" + str(len(remote_noncoding02)) + "\n")
remote_noncoding02_out.write(remote_noncoding02)
remote_noncoding02_out.close()
print(open("remote_noncoding02.fasta").read())
local_exon01_out = open("local_exon01.fasta", "w")
local_exon01_out.write(">LocalSeq_exon01_length" + str(len(local_exon01)) + "\n")
local_exon01_out.write(local_exon01)
local_exon01_out.close()
print(open("local_exon01.fasta").read())
local_intron01_out = open("local_intron01.fasta", "w")
local_intron01_out.write(">LocalSeq_intron01_length" + str(len(local_intron01)) + "\n")
local_intron01_out.write(local_intron01)
local_intron01_out.close()
print(open("local_intron01.fasta").read())
local_exon02_out = open("local_exon02.fasta", "w")
local_exon02_out.write(">LocalSeq_exon02_length" + str(len(local_exon02)) + "\n")
local_exon02_out.write(local_exon02)
local_exon02_out.close()
print(open("local_exon02.fasta").read())
exons_out = open("All_exons.fasta", "w")
exons_out.write(">AJ223353_exon01_length" + str(len(remote_exon01)) + "\n" + remote_exon01 + "\n")
exons_out.write(">LocalSeq_exon01_length" + str(len(local_exon01)) + "\n" + local_exon01 + "\n")
exons_out.write(">LocalSeq_exon02_length" + str(len(local_exon02)) + "\n" + local_exon02)
exons_out.close()
print(open("All_exons.fasta").read())
introns_out = open("All_noncodings.fasta", "w")
introns_out.write(">AJ223353_noncoding01_length" + str(len(remote_noncoding01)) + "\n" + remote_noncoding01 + "\n")
introns_out.write(">AJ223353_noncoding02_length" + str(len(remote_noncoding02)) + "\n" + remote_noncoding02 + "\n")
introns_out.write(">LocalSeq_intron01_length" + str(len(local_intron01)) + "\n" + local_intron01)
introns_out.close()
print(open("All_noncodings.fasta").read())