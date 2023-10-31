ls -1 *.fasta*
grep ">" All_exons.fasta
grep ">" All_noncodings.fasta
blastx -db databasename -query fastafilename -outfmt 7
blastx -db databasename -query fastafilename -outfmt 7 | head -n6

blastx -db '/localdisk/home/aivens2/Exercises/Lecture06/nem' -query 'All_exons.fasta' -outfmt 6 -num_alignments 1 > quick_blast_check.out
cat quick_blast_check.out
