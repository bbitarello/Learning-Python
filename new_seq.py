# 19 3'UTR
# 63 exon1
# 27 introns
# 36 exon2
# 22 5'UTR

new_seq = "TGGCGTGAACGTTGCACGTATGGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGA\
TCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTATTAATGGCGTGCGAACATGCGCACGT"


#cut the sequence into its different elements

utr3 = new_seq[0:19] #19

exon1 = new_seq[19:19+63] #63

introns = new_seq[19+63:19+63+27] #27

exon2 = new_seq[19+63+27:19+63+27+36] #36

utr5 = new_seq[19+63+27+36:] #22
#control that the coding sequence is "translatable"

CDS = exon1 + exon2

len(CDS) %3 == 0


utr3 + exon1 + introns + exon2 + utr5 == new_seq
#verify that the coding sequence starts with a methionine (ATG) and ends by a stop codon ('TAA')

exon1.startswith('ATG') and exon2.endswith('TAA')

