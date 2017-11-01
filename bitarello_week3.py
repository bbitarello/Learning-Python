#PROCESSING DNA IN A FILE

#The file input.txt contains a number of DNA sequences, one per line. Each sequence starts
#with the same 14 base pair fragment – a sequencing adapter that should have been removed. 
#Write a program that will (a) trim this adapter and write the cleaned sequences to a new 
#file and (b) print the length of each sequence to the screen.


#open file

file = open("input.txt", "r")

all_lines = file.readlines()

OUT =  open("outfile.txt", "w")

for aline in all_lines:
	print("the length of this sequence is " + str(len(aline[14:].replace("\n",""))))
	OUT.write(aline[14:])
	
OUT.close()	


####

#MULTIPLE EXONS FROM GENOMIC DNA

#The file genomic_dna.txt contains a section of genomic DNA, and the file exons.txt 
#contains a list of start/stop positions of exons. Each exon is on a separate line and the
# start and stop positions are separated by a comma. The start and stop positions follow 
#Python conventions; they start from zero and are inclusive at the start and exclusive at 
#the end. Write a program that will extract the exon segments, concatenate them, and write
# them to a new file.

#This is a tricky exercise with several parts: your program will have to:

#read the exon file line by line

exons = open("exons.txt", "r")
exons_all_lines = exons.readlines()

genomic = open("genomic_dna.txt","r").read()
#split each exon line into two numbers

OUT = open("out_seq.txt", "w")

for aline in exons_all_lines:
	beg =int(aline.split(",")[0])
	end = int(aline.split(",")[1]) #turn those numbers into integers
	OUT.write(genomic[beg:end]) #extract the matching part of the genomic DNA sequence. #concatenate all the exon sequences together
	

OUT.close()	
