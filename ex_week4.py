#Copy and paste this chunk of code into a new program, then use this dict to write a 
#program which will translate a DNA sequence into protein. You'll have to figure out how to:

#split the DNA sequence into codons
#look up the amino acid residue for each codon
#join all the amino acids to give a protein
#Test your program on a couple of different inputs to see what happens. How does your program 
#cope with a sequence whose length is not a multiple of 3? How does it cope with a sequence that contains unknown bases?

gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
    
    
my_seq = 'ATGGCCAGGAAGTGATGGGCCTCATAGCACGAGCGTGAATAAAACATTCAC'

all_aminoacids = ''

if(len(my_seq) % 3 == 0):
	for i in range(0, len(my_seq),3):

		codon = my_seq[i:i+3]

		all_aminoacids += gencode[codon]
	
if(	len(my_seq) % 3 != 0):
	for i in range(0, (len(my_seq)-3),3):
		codon = my_seq[i:i+3]

		all_aminoacids += gencode[codon]
	
