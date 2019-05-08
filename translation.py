#!/usr/bin/env python2
#This program translate nucleotides to amino acid

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

# create a random file name mydna.txt 

l = open('mydna.txt','w')
l.write('TGAGATGGCTTATTGGGT')
l.close()

dna = open('mydna.txt','r')
dnaRead = dna.readline()
print("The original complete sequence:")
print(dnaRead)

#If can't divide by 3 -> out put the two letters and run the rest of the input into translation
def read_codons(dna):
    codons = []
    began = False
    for i in range(0, len(dna)-2, 3):
        segment = dna[i:i+3]
        next_codon = gencode[segment]
        if next_codon == '_': #stop codon?
            if began == True: #are we already reading?
                return codons #stop encoding
            else: #ignore the stop codon at the beginning
                continue
        else:
            began = True
            codons.append( next_codon )
    return codons

print("Post translation sequence:")
# I am trying to make the output a string not list. 
print("".join(read_codons(dnaRead)) )
