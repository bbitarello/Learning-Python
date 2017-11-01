#CALCULATING AT CONTENT

#Here's a short DNA sequence:

#ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
#Write a program that will print out the AT content of this DNA sequence (i.e. the proportion of bases that are either A or T). Hint: you can use normal mathematical symbols like add (+), subtract (-), multiply (*), divide (/) and parentheses to carry out calculations on numbers in Python.

my_string = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

nA = my_string.count('A')
nC = my_string.count('C')
nG = my_string.count('G')
nT = my_string.count('T')

result = nA+nT/len(my_string)
print(result)


#COMPLEMENTING DNA

#Here's a short DNA sequence:

#ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
#Write a program that will print the complement of this sequence. To find the complement we replace each base with its pair: A with T, T with A, C with G and G with C.

my_string = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

tmp = my_string.replace('A','A2')
tmp2 = tmp.replace('T','A')
tmp3 = tmp2.replace('A2','T')
tmp4 = tmp3.replace('C','C2')
tmp5 = tmp4.replace('G','C')
result = tmp5.replace('C2', 'G') 

print(result)





#RESTRICTION FRAGMENT LENGTHS

#Here's a short DNA sequence:

#ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT
#The sequence contains a recognition site for the EcoRI restriction enzyme, which cuts at the motif G*AATTC (the position of the cut is indicated by an asterisk). Write a program which will calculate the size of the two fragments that will be produced when the DNA sequence is digested with EcoRI.

my_string = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'

first_len = 1+ my_string.find('GAATTC') 

second_len = len(my_string) - first_len


print(first_len) #22
print(second_len) #33



###
#SPLICING OUT INTRONS, PART ONE

#Here's a short section of genomic DNA:

#ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT
#It comprises two exons and an intron. The first exon runs from the start of the sequence to base number 63 (starting counting from zero), and the second exon runs from base 91 (also counting from zero) to the end of the sequence. Write a program that will print just the coding regions of the DNA sequence.


my_string = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'

result = my_string[0:63] + my_string[91:] #should be 90 instead of 91.






#SPLICING OUT INTRONS, PART TWO

#Using the data from part one, write a program that will calculate what percentage of the DNA sequence is coding.

my_string = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'


coding = my_string[0:63] + my_string[91:]

result = len(coding)/len(my_string)

print(result)


#SPLICING OUT INTRONS, PART THREE

#Using the data from part one, write a program that will print out the original genomic DNA sequence with coding bases in uppercase and non-coding bases in lowercase.

my_string[64:90]

result = my_string[0:63] + my_string[64:90].lower() + my_string[91:]  #should be [63:90] and [90:]

print(result)


