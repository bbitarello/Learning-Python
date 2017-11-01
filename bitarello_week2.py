#SPLITTING GENOMIC DNA

#Look at the file called genomic_dna.txt – it contains the same piece of genomic DNA that we were using in the final exercise from the previous page. 
#Write a program that will split the genomic DNA into coding and non-coding parts, and write these sequences to two separate files.

#answer

#in the last exercise of chap 1 we had the following info:

#It comprises two exons and an intron. The first exon runs from the start of the sequence to base number 63 (starting counting from zero), and the second exon runs from base 91 (also counting from zero) to the end of the sequence. 


genomic_dna = open('genomic_dna.txt').read().rstrip('\n')



coding = genomic_dna[0:63] + genomic_dna[90:]

non_coding = genomic_dna[63:90]

out1 = open('out_coding.txt', 'w')
out2 = open('out_non_coding.txt','w')

out1.write(coding)
out2.write(non_coding)

out1.close()
out2.close()



###Second exercise

#Write a program that will create a FASTA file for the following three sequences – make sure that all sequences are in uppercase and only contain the bases A, T, G and C.

#Sequence header	DNA sequence
#ABC123	ATCGTACGATCGATCGATCGCTAGACGTATCG
#DEF456	actgatcgacgatcgatcgatcacgact
#HIJ789	ACTGAC-ACTGT--ACTGTA----CATGTG


fasta_out = open('out_fasta.txt','w')

fasta_out.write(">ABC123\n" + "ATCGTACGATCGATCGATCGCTAGACGTATCG")

fasta_out.write("\n>DEF456\n" + "actgatcgacgatcgatcgatcacgact".upper())

fasta_out.write("\n>HIJ789\n" + "ACTGAC-ACTGT--ACTGTA----CATGTG".replace("-",""))

fasta_out.close()

#Third exercise

#WRITING MULTIPLE FASTA FILES

#Use the data from the previous exercise, but instead of creating a single FASTA file, create three new FASTA files – one per sequence. The names of the FASTA files should be the same as the sequence header names, with the extension .fasta.

fasta1 = open('ABC123.fasta','w')
fasta2 = open('DEF456.fasta','w')
fasta3 = open('HIJ789.fasta','w')

fasta1.write(">ABC123\n" + "ATCGTACGATCGATCGATCGCTAGACGTATCG")
fasta1.close()

fasta2.write(">DEF456\n" + "actgatcgacgatcgatcgatcacgact".upper())
fasta2.close()

fasta3.write(">HIJ789\n" + "ACTGAC-ACTGT--ACTGTA----CATGTG".replace("-",""))
fasta3.close()