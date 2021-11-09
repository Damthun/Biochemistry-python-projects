
from typing import List
import os as os
os.chdir("C:\\Users\\trunk\\PycharmProjects\\Biochem")
input_file = open('Sequence.txt','r')
Sequence = input_file.read()

input_file.close()
# AAGATTAATGACAATGAGATTCATCAGTTTAACAAAAACAACTCCAATCAAGCAGTAGCTGTAACTTTCACAAAGTGTGAAGAAGAACCTTTAGATTTAATTACAAGTCTTCAGAATGCCAGAGATATACAGGATATGCGAATTAAGAAGAA\
# ACAAAGGCAACGCGTCTTTCCACAGCCAGGCAGTCTGTATCTTGCAAAAACATCCACTCTGCCTCGAATCTCTCTGAAAGCAGCAGTAGGAGGCCAAGTTCCCTCTGCGTGTTCTCATAAACAGCTGTATACGTATGGCGTTTCTAAACATTG\
# CATAAAAATTAACAGCAAAAATGCAGAGTCTTTTCAGTTTCACACTGAAGATTATTTTGGTAAGGAAAGTTTATGGACTGGAAAAGGAATACAGTTGGCTGATGGTGGATGGCTCAT\
# ACCCTCCAATGATGGAAAGGCTGGAAAAGAAGAATTTTATAGGGCTCTGTGTGACACTCCAGGTGTGGAT\
# CCAAAGCTTATTTCTAGAATTTGGGTTTATAATCACTATAGATGGATCATATGGAAACTGGCAGCTATGG\
# AATGTGCCTTTCCTAAGGAATTTGCTAATAGATGCCTAAGCCCAGAAAGGGTGCTTCTTCAACTAAAATA\
# CAGATATGATACGGAAATTGATAGAAGCAGAAGATCGGCTATAAAAAAGATAATGGAAAGGGATGACACA\
# GCTGCAAAAACACTTGTTCTCTGTGTTTCTGACATAATTTCATTGAGCGCAAATATATCTGAAACTTCTA\
# GCAATAAAACTAGTAGTGCAGATACCCAAAAAGTGGCCATTATTGAACTTACAGATGGGTGGTATGCTGT\
# TAAGGCCCAGTTAGATCCTCCCCTCTTAGCTGTCTTAAAGAATGGCAGACTGACAGTTGGTCAGAAGATT\
# ATTCTTCATGGAGCAGAACTGGTGGGCTCTCCTGATGCCTGTACACCTCTTGAAGCCCCAGAATCTCTTA\
# TGTTAAAGATTTCTGCTAACAGTACTCGGCCTGCTCGCTGGTATACCAAACTTGGA'

stop_codons = ['UGA', 'UAA', 'UAG']
Upper = Sequence.upper()
SequencePos = Upper.replace('T', 'U')   # replaces all T's with U's I would convert to complementary then to RNA but this saves me a few loops.
pFrame1 = SequencePos
pFrame2 = SequencePos[1:-2]
pFrame3 = SequencePos[2:-1]

b = len(Sequence)/3

pstops = []
pf1_stops = []
pf2_stops = []
pf3_stops = []

pf1_starts = []
pf2_starts = []
pf3_starts = []

pf1_pairs = [[],[]]
pf2_pairs = [[],[]]
pf3_pairs = [[],[]]

for k in range(int(b)*3):

    current_codon = pFrame1[k:k+3]
    if current_codon in stop_codons:
        pstops.append(k)
pPossible_1 = [(x)/3 for x in pstops]
pPossible_2 = [(x+1)/3 for x in pstops]
pPossible_3 = [(x+2)/3 for x in pstops]
for i in range(len(pstops)):

    if pPossible_1[i].is_integer():
        pf1_stops.append(3*int(pPossible_1[i]))
    if pPossible_2[i].is_integer():
        pf2_stops.append(3*int(pPossible_2[i])-1)
    if pPossible_3[i].is_integer():
        pf3_stops.append(3*int(pPossible_3[i])-2)

# FRAME ONE
print('**********************************************************************************************************************************************************')
for i in range(int(b)):
    if pFrame1[3*i:3*i + 3] == 'AUG':
        pf1_starts.append(3*i)

if len(pf1_starts)>0:
    print("Hey, I've found at  least one start codon in frame ONE of the positive sequence, they can be found in this list!" + str(pf1_starts)+ '\n\n')

elif len(pf1_starts)==0:
    print("Shoot, no start codons here!")

for x in pf1_stops:
    for y in pf1_starts:

        if x >y and (x-y)> 150:
            pf1_pairs[0].append(y)
            pf1_pairs[1].append(x)
if len(pf1_pairs[0]) >0:
    print('I have found at least one pair of start and stop codons in frame ONE of the positive sequence that could constitue a string, \nStarting at # '+ str(pf1_pairs[0])+' \nending at    # ' +str(pf1_pairs[1]))


elif len(pf1_pairs[0]) == 0:
    print('Dang, no start and end pairs that fit our criteria of 50 codons long :c')
# FRAME TWO
print('**********************************************************************************************************************************************************')


for i in range(int(b)-3):
    if pFrame2[3*i:3*i + 3] == 'AUG':

        pf2_starts.append(3*i+1)
if len(pf2_starts)>1:
    print("Hey, I've found at  least one start codon in frame TWO of the positive sequence, they can be found in this list!" + str(pf2_starts)+ '\n\n')
elif len(pf2_starts)==0:
    print("Shoot, no start codons here!")
for x in pf2_stops:
    for y in pf2_starts:
        if x >y and (x-y)> 150:
            pf2_pairs[0].append(y)
            pf2_pairs[1].append(x)
if len(pf2_pairs[0]) >0:
    print('I have found at least one pair of start and stop codons in frame TWO of the positive sequence that could constitue a string, \nStarting at # '+ str(pf2_pairs[0])+' \nending at    # ' +str(pf2_pairs[1]))


elif len(pf2_pairs[0]) == 0:
    print('Dang, no start and end pairs that fit our criteria of 50 codons long :c')
#frame THREE
print('**********************************************************************************************************************************************************')

for i in range(int(b)-3):
    if pFrame3[3*i:3*i+ 3] == 'AUG':
        pf3_starts.append(3*i+2)

if len(pf3_starts)>1:
    print("Hey, I've found at  least one start codon in frame THREE of the positive sequence, they can be found in this list!" + str(pf3_starts)+ '\n\n')

elif len(pf1_starts) == 0:
    print("Shoot, no start codons here!")

for x in pf3_stops:
    for y in pf3_starts:
        if x >y and (x-y)> 150:
            pf3_pairs[0].append(y)
            pf3_pairs[1].append(x)

if len(pf3_pairs[0]) >0:
    print('I have found at least one pair of start and stop codons in frame THREE of the positive sequence that could constitue a string, \nStarting at # '+ str(pf3_pairs[0])+' \nending at    # ' +str(pf3_pairs[1]))



elif len(pf3_pairs[0]) == 0:
    print('Dang, no start and end pairs that fit our criteria of 50 codons long :c')
print('**********************************************************************************************************************************************************\n')
print('**********************************************************************************************************************************************************')
print('**********************************************************************************************************************************************************\n\n')
Sequencel = SequencePos.lower()
T = Sequencel.replace('u', 'A')
A = T.replace('a', 'U')
G = A.replace('g', 'C')
SequenceNeg = G.replace('c', 'G')
#print(SequenceNeg)








nFrame1 = SequenceNeg
nFrame2 = SequenceNeg[1:-2]
nFrame3 = SequenceNeg[2:-1]

b = len(Sequence)/3

nstops = []
nf1_stops = []
nf2_stops = []
nf3_stops = []

nf1_starts = []
nf2_starts = []
nf3_starts = []

nf1_pairs=[[],[]]
nf2_pairs=[[],[]]
nf3_pairs=[[],[]]

for k in range(int(b)*3):

    current_codon = nFrame1[k:k+3]
    if current_codon in stop_codons:
        nstops.append(k)
nPossible_1 = [(x)/3 for x in nstops]
nPossible_2 = [(x+1)/3 for x in nstops]
nPossible_3 = [(x+2)/3 for x in nstops]
for i in range(len(nstops)):
    if nPossible_1[i].is_integer() :
        nf1_stops.append(int(nPossible_1[i]))
    if nPossible_2[i].is_integer():
        nf2_stops.append(int(nPossible_2[i])-1)
    if nPossible_3[i].is_integer():
        nf3_stops.append(int(nPossible_3[i])-2)
# FRAME ONE
print('**********************************************************************************************************************************************************')
for i in range(int(b)):
    if nFrame1[3 * i:3 * i + 3] == 'AUG':
        nf1_starts.append(3*i)

if len(nf1_starts)>0:
    print("Hey, I've found at  least one start codon in frame ONE of the negative sequence, they can be found in this list!" + str(nf1_starts)+ '\n\n')

elif len(nf1_starts)==0:
    print("Shoot, no start codons here!")

for x in nf1_stops:
    for y in nf1_starts:
        if x >y and (x-y)> 150:
            nf1_pairs[0].append(y)
            nf1_pairs[1].append(x)
if len(nf1_pairs[0]) >0:
    print('I have found at least one pair of start and stop codons in frame ONE of the NEGATIVE sequence that could constitue a string, \nStarting at # '+ str(nf1_pairs[0])+' \nending at    # ' +str(nf1_pairs[1]))


elif len(nf1_pairs[0]) == 0:
    print('Dang, no start and end pairs that fit our criteria of 50 codons long :c')
# FRAME TWO
print('**********************************************************************************************************************************************************')


for i in range(int(b)-3):
    if nFrame2[3 * i:3 * i + 3] == 'AUG':

        nf2_starts.append(3*i+1)
if len(nf2_starts)>1:
    print("Hey, I've found at  least one start codon in frame TWO of the NEGATIVE sequence, they can be found in this list!" + str(nf2_starts)+ '\n\n')
elif len(nf2_starts)==0:
    print("Shoot, no start codons here!")
for x in nf2_stops:
    for y in nf2_starts:
        if x >y and (x-y)> 150:
            nf2_pairs[0].append(y)
            nf2_pairs[1].append(x)
if len(nf2_pairs[0]) >0:
    print('I have found at least one pair of start and stop codons in frame TWO of the NEGATIVE sequence that could constitue a string, \nStarting at # '+ str(nf2_pairs[0])+' \nending at    # ' +str(nf2_pairs[1]))

elif len(nf2_pairs[0]) == 0:
    print('Dang, no start and end pairs that fit our criteria of 50 codons long :c')
#frame THREE
print('**********************************************************************************************************************************************************')

for i in range(int(b)-3):
    if nFrame3[3 * i:3 * i + 3] == 'AUG':
        nf3_starts.append(3*i+2)

if len(nf3_starts)>1:
    print("Hey, I've found at  least one start codon in frame THREE of the NEGATIVE sequence, they can be found in this list!" + str(nf3_starts)+ '\n\n')

elif len(nf1_starts) == 0:
    print("Shoot, no start codons here!")

for x in nf3_stops:
    for y in nf3_starts:
        if x >y and (x-y)> 150:
            nf3_pairs[0].append(y)
            nf3_pairs[1].append(x)

if len(nf3_pairs[0]) >0:
    print('I have found at least one pair of start and stop codons in frame THREE of the NEGATIVE sequence that could constitue a string, \nStarting at # '+ str(nf3_pairs[0])+' \nending at    # ' +str(nf3_pairs[1]))


elif len(nf3_pairs[0]) == 0:
    print('Dang, no start and end pairs that fit our criteria of 50 codons long :c')
print('**********************************************************************************************************************************************************')

All_pairs = [pf1_pairs, pf2_pairs, pf3_pairs, nf1_pairs, nf2_pairs, nf3_pairs]

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]
AAchain=[]
for x in All_pairs:

    if (namestr(x,globals())[1][0]) == 'n':
        if len(x[1])>0:


            for k in range(len(x[0])):
                AAchain = []
                l = int((x[1][k] - x[0][k]) / 3)
                L = l+1
                numORF = k
                Frame = (namestr(x,globals()))[1][2]
                for i in range(l+1):


                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UCU' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UCC' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UCA' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UCG' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AGU' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AGC':
                        AAchain.append('S')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CUU' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CUC' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CUA' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CUG':
                        AAchain.append('L')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GUU' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GUC' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GUA' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GUG':
                        AAchain.append('V')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GCU' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GCC' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GCA' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GCG':
                        AAchain.append('A')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CCU' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CCC' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CCA' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CCG':
                        AAchain.append('P')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GGU' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GGC' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GGA' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GGG':
                        AAchain.append('G')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CGU' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CGC' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CGA' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CGG':
                        AAchain.append('R')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'ACU' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'ACC' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'ACA' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'ACG':
                        AAchain.append('T')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UUU' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UUC':
                        AAchain.append('F')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UUA' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UUG':
                        AAchain.append('L')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UAU' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UAC':
                        AAchain.append('Y')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UAA' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UAG' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UGA':
                        AAchain.append('*')

                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UGU' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UGC':
                        AAchain.append('C')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UGG':
                        AAchain.append('W')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CAU' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CAC':
                        AAchain.append('H')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CAA' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CAG':
                        AAchain.append('Q')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AAU' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AAC':
                        AAchain.append('N')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AAA' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AAG':
                        AAchain.append('K')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GAU' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GAC':
                        AAchain.append('D')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GAA' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GAG':
                        AAchain.append('E')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AGA' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AGG':
                        AAchain.append('R')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AUU' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AUC' or SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AUA':
                        AAchain.append('I')
                    if SequenceNeg[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AUG':
                        AAchain.append('M')
                chain = ''.join(AAchain)

                if chain.count('*') == 1:
                    print('ORF #%d  |  Strand: Negative  |  Frame: %d  | Length: %d \n%s' % (int(numORF), int(Frame), L, chain))

    else:

        if len(x[1])>0:

            for k in range(len(x[0])):
                AAchain = []
                l = int((x[1][k]-x[0][k])/3)
                L = l+1

                numORF = k
                Frame = (namestr(x,globals()))[0][2]

                for i in range(l+1):


                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UCU' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UCC' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UCA' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UCG' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AGU' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AGC':
                        AAchain.append('S')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CUU' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CUC' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CUA' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CUG':
                        AAchain.append('L')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GUU' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GUC' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GUA' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GUG':
                        AAchain.append('V')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GCU' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GCC' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GCA' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GCG':
                        AAchain.append('A')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CCU' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CCC' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CCA' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CCG':
                        AAchain.append('P')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GGU' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GGC' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GGA' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GGG':
                        AAchain.append('G')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CGU' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CGC' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CGA' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CGG':
                        AAchain.append('R')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'ACU' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'ACC' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'ACA' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'ACG':
                        AAchain.append('T')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UUU' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UUC':
                        AAchain.append('F')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UUA' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UUG':
                        AAchain.append('L')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UAU' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UAC':
                        AAchain.append('Y')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UAA' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UAG' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UGA':
                        AAchain.append('*')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UGU' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UGC':
                        AAchain.append('C')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'UGG':
                        AAchain.append('W')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CAU' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CAC':
                        AAchain.append('H')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CAA' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'CAG':
                        AAchain.append('Q')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AAU' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AAC':
                        AAchain.append('N')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AAA' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AAG':
                        AAchain.append('K')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GAU' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GAC':
                        AAchain.append('D')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GAA' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'GAG':
                        AAchain.append('E')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AGA' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AGG':
                        AAchain.append('R')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AUU' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AUC' or SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AUA':
                        AAchain.append('I')
                    if SequencePos[x[0][k]+(3*i):x[0][k]+(3*i)+3] == 'AUG':
                        AAchain.append('M')
                chain = ''.join(AAchain)


                if chain.count('*') == 1:
                    print('ORF #%d  |  Strand: Positive  |  Frame: %d  | Length: %d \n%s' % (int(numORF), int(Frame), L, chain))





