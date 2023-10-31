input_txt_contents = open('input.txt').read().upper().replace('ATTCGATTATAAGC','').split()
input_txt_contents2 = open('input.txt').read().upper().split()
len(input_txt_contents)
len(input_txt_contents2)
cleanseqs = open('Cleaned_sequences.txt','w')
for cleanones in input_txt_contents :
    cleanseqs.write(cleanones + '\n')
    cleanones
cleanseqs.close()
print(open('Cleaned_sequences.txt').read().rstrip())

import subprocess
subprocess.call("cat Cleaned_sequences.txt",shell=True)
