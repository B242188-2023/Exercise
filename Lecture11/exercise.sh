grep -v ">" AJ223353.fasta > AJ223353_noheader.fasta
esearch -db nucleotide -query "AJ223353[accession]" | efetch -format fasta | grep -v ">" > AJ223353_noheader.fasta2
esearch -db nucleotide -query "AJ223353[accession]" | efetch -format gb > AJ223353.genbank
esearch -db nucleotide -query "AJ223353[accession]" | efetch -format gb | grep "CDS"