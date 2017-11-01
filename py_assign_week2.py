with open('out_fasta.txt', 'r') as genomic_dna:
	header_1 = genomic_dna.readline()
	seq_1 = genomic_dna.readline()
	header_2 = genomic_dna.readline()
	seq_2 = genomic_dna.readline()
	header_3 = genomic_dna.readline()
	seq_3 = genomic_dna.readline()

print(genomic_dna.closed)


# Combine with and for

with open('out_fasta.txt', 'r') as fastas:
	for line in fastas:
		print(line, end="") #could also have used print(line.rstrip('\n'))
#close for
#close with
print(fastas.closed)

#the if statement: using if, with and for, in your threes equences file, print only the sequences that start with "ACT"


with open('out_fasta.txt', 'r') as fastas:
	for line in fastas:
		if(line.startswith('ACT')):

			print(line, end="")

	



with open('out_fasta.txt', 'r') as fastas:
	for line in fastas:
		if(line.startswith(">")):
			header = line
		if(line.startswith('ACT')):	
			print(header, end="")
			print(line,end="")
			


		