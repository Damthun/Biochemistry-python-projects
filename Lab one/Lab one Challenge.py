
SequenceDNA = input("Need an AA chain? give me that DNA!")
SequenceDNAU = SequenceDNA.upper()
if SequenceDNAU.find('B') != -1 or SequenceDNAU.find('D') != -1 or SequenceDNAU.find('E') != -1 or SequenceDNAU.find('F') != -1 or SequenceDNAU.find('P') != -1 or SequenceDNAU.find('H') != -1 or SequenceDNAU.find('I') != -1 or SequenceDNAU.find('J') != -1 or SequenceDNAU.find('K') != -1 or SequenceDNAU.find('L') != -1 or SequenceDNAU.find('M') != -1 or SequenceDNAU.find('N') != -1 or SequenceDNAU.find('O') != -1 or SequenceDNAU.find('Q') != -1 or SequenceDNAU.find('R') != -1 or SequenceDNAU.find('S') != -1 or SequenceDNAU.find('U') != -1 or SequenceDNAU.find('V') != -1 or SequenceDNAU.find('W') != -1 or SequenceDNAU.find('W') != -1 or SequenceDNAU.find('X') != -1 or SequenceDNAU.find('Y') != -1 or SequenceDNAU.find('Z') != -1:
    print("Your DNA Sequence is invalid... Try again using only the letters T, A, G & C.")

Sequence = SequenceDNAU.replace('T', 'U')   # replaces all T's with U's I would convert to complementary then to RNA but this saves me a few loops.
b = len(Sequence)/3
### THIS SUCKS, COULD BE DONE BETTER BUT STILL

SequenceU = Sequence.upper()
AAchain = []

if float(b).is_integer():

    for i in range(int(b)):
        #print(3*i)

        if SequenceU[3*i:3*i+3] == 'UCU' or SequenceU[3*i:3*i+3] == 'UCC' or SequenceU[3*i:3*i+3] == 'UCA' or SequenceU[3*i:3*i+3] == 'UCG' or SequenceU[3*i:3*i+3] == 'AGU' or SequenceU[3*i:3*i+3] == 'AGC':
            AAchain.append('Ser')
        if SequenceU[3*i:3*i+3] == 'CUU' or SequenceU[3*i:3*i+3] == 'CUC' or SequenceU[3*i:3*i+3] == 'CUA' or SequenceU[3*i:3*i+3] == 'CUG':
            AAchain.append('Leu')
        if SequenceU[3*i:3*i+3] == 'GUU' or SequenceU[3*i:3*i+3] == 'GUC' or SequenceU[3*i:3*i+3] == 'GUA' or SequenceU[3*i:3*i+3] == 'GUG':
            AAchain.append('Val')
        if SequenceU[3*i:3*i+3] == 'GCU' or SequenceU[3*i:3*i+3] == 'GCC' or SequenceU[3*i:3*i+3] == 'GCA' or SequenceU[3*i:3*i+3] == 'GCG':
            AAchain.append('Ala')
        if SequenceU[3*i:3*i+3] == 'CCU' or SequenceU[3*i:3*i+3] == 'CCC' or SequenceU[3*i:3*i+3] == 'CCA' or SequenceU[3*i:3*i+3] == 'CCG':
            AAchain.append('Pro')
        if SequenceU[3*i:3*i+3] == 'GGU' or SequenceU[3*i:3*i+3] == 'GGC' or SequenceU[3*i:3*i+3] == 'GGA' or SequenceU[3*i:3*i+3] == 'GGG':
            AAchain.append('Gly')
        if SequenceU[3*i:3*i+3] == 'CGU' or SequenceU[3*i:3*i+3] == 'CGC' or SequenceU[3*i:3*i+3] == 'CGA' or SequenceU[3*i:3*i+3] == 'CGG':
            AAchain.append('Arg')
        if SequenceU[3*i:3*i+3] == 'ACU' or SequenceU[3*i:3*i+3] == 'ACC' or SequenceU[3*i:3*i+3] == 'ACA' or SequenceU[3*i:3*i+3] == 'ACG':
            AAchain.append('Thr')
        if SequenceU[3*i:3*i+3] == 'UUU' or SequenceU[3*i:3*i+3] == 'UUC':
            AAchain.append('Phe')
        if SequenceU[3*i:3*i+3] == 'UUA' or SequenceU[3*i:3*i+3] == 'UUG':
            AAchain.append('Leu')
        if SequenceU[3*i:3*i+3] == 'UAU' or SequenceU[3*i:3*i+3] == 'UAC':
            AAchain.append('Tyr')
        if SequenceU[3*i:3*i+3] == 'UAA' or SequenceU[3*i:3*i+3] == 'UAG' or SequenceU[3*i:3*i+3] == 'UGA':
            AAchain.append('*')
        if SequenceU[3*i:3*i+3] == 'UGU' or SequenceU[3*i:3*i+3] == 'UGC':
            AAchain.append('Cys')
        if SequenceU[3*i:3*i+3] == 'UGG':
            AAchain.append('Trp')
        if SequenceU[3*i:3*i+3] == 'CAU' or SequenceU[3*i:3*i+3] == 'CAC':
            AAchain.append('His')
        if SequenceU[3*i:3*i+3] == 'CAA' or SequenceU[3*i:3*i+3] == 'CAG':
            AAchain.append('Gln')
        if SequenceU[3*i:3*i+3] == 'AAU' or SequenceU[3*i:3*i+3] == 'AAC':
            AAchain.append('Asn')
        if SequenceU[3*i:3*i+3] == 'AAA' or SequenceU[3*i:3*i+3] == 'AAG':
            AAchain.append('Lys')
        if SequenceU[3*i:3*i+3] == 'GAU' or SequenceU[3*i:3*i+3] == 'GAC':
            AAchain.append('Asp')
        if SequenceU[3*i:3*i+3] == 'GAA' or SequenceU[3*i:3*i+3] == 'GAG':
            AAchain.append('Glu')

        if SequenceU[3*i:3*i+3] == 'AGA' or SequenceU[3*i:3*i+3] == 'AGG':
            AAchain.append('Arg')
        if SequenceU[3*i:3*i+3] == 'AUU' or SequenceU[3*i:3*i+3] == 'AUC' or SequenceU[3*i:3*i+3] == 'AUA':
            AAchain.append('ILe')
        if SequenceU[3*i:3*i+3] == 'AUG':
            AAchain.append('Met')


chain = '-'.join(AAchain)
print(chain)