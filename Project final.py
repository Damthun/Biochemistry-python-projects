import numpy as np

AAchain = input("I Need an AA chain if you want those stats.")
uAAchain = AAchain.upper()  # user proofing the input, will work with upper case letters
#print(AAchain[-1:])
#print(AAchain[0])
Actual_chain_length = 0
# [AA, Count, Mass, COOH, NH3] This set of nested lists hold the amount of each amino acid, as well as their weight and the pKa's of their carboxylic acid and amine groups.
possibleAA = [['A', 0, 89, 2.34, 9.69], ['R', 0, 174, 2.17, 9.04], ['N', 0, 132, 2.02, 8.80], ['D', 0, 133, 1.88, 9.60],
              ['C', 0, 121, 1.96, 10.28], ['Q', 0, 146, 2.17, 9.13], ['E', 0, 147, 2.19, 9.67], ['G', 0, 75, 2.34, 9.60],
              ['H', 0, 155, 1.82, 9.17], ['I', 0, 131, 2.36, 9.68], ['L', 0, 131, 2.36, 9.60], ['K', 0, 146, 2.18, 8.95],
              ['M', 0, 149, 2.28, 9.21], ['F', 0, 165, 1.83, 9.13], ['P', 0, 115, 1.99, 10.96], ['S', 0, 105, 2.21, 9.15],
              ['T', 0, 119, 2.11, 9.62], ['W', 0, 204, 2.38, 9.39], ['Y', 0, 181, 2.20, 9.11], ['V', 0, 117, 2.32, 9.62]]



RgroupWpKa = [['Y', 10.07], ['D', 3.65], ['C', 8.18], ['E', 9.67], ['H', 6.00], ['K', 10.53],
              ['R', 12.48]]  # this names each of the amino acids with R groups that have a pKa and lists their pKa's.

#print(len(possibleAA))
# COUNTING EACH AMINO ACID
for i in range(len(possibleAA)): # for each amino acid 1-20
    possibleAA[i][1] = uAAchain.count(possibleAA[i][0]) # please set the second count value in each nested list to how many times we see that AA in the chain.

# CALCULATING ACTUAL CHAIN LENGTH; Reason of this is because of human error, a chain of AAJ would offset the molar mass calculation by 18 as the chain length changes the molar mass by 18 per diff AA length.
for i in range(len(possibleAA)):  # for each amino acid 1-20

    Actual_chain_length = Actual_chain_length + possibleAA[i][1] # please add how many of each amino acid to the total chain length. this will make sure no J's, Z's, 9's or any other non AA code ruin the code.
print('Actual chain length is : ' + str(Actual_chain_length))

## MOLAR MASS CALCULATION
molar_mass = (-18* (Actual_chain_length-1)) # this offsets the fact that peptide bond formation is hydrolysis (-H2O) so a 1 AA wouldn't be offset but 2 would be (m1 + m2)-18 = mAAchain
for i in range(len(possibleAA)):
    molar_mass = molar_mass + (possibleAA[i][1] * possibleAA[i][2]) # take the offset molar mass variable and add the product of molar mass (3rd object in each nested list) and # of AA in that chain(2nd object in nested lists).
print('The molar mass is : ' + str(molar_mass))

## Max charge calculator
Max_charge = 1
Min_charge = -1
for i in range(3):
    Max_charge = Max_charge + uAAchain.count(RgroupWpKa[i+4][0])  # so the max charge is 1 (NH3 on end AA) + 1 per any of the 3 (reason why range is 3) AA's KHR (they have a potentially pos. R group.)
print('The maximum charge is : +' + str(Max_charge))
for i in range(4):
    Min_charge = Min_charge - uAAchain.count(RgroupWpKa[i][0]) # min charge is similar except we are subtracting one for each one of the EDCY AA's
print('The minimum charge is : ' + str(Min_charge))

######## THIS IS FOR THE ISOELECTRIC POINT ################
pKaList = [] # we want a list of pKas that will help us estimate pI
firstAA = uAAchain[0] # we're grabbing the first and last AA's as they are the only ones to have alpha pKa's if that makes sense.
lastAA = uAAchain[-1:]
#print(firstAA)
#print(lastAA)
for i in range(len(possibleAA)):
    if firstAA.count(possibleAA[i][0]) != 0:
        pKaList.append(possibleAA[i][4])   # so we are checking each amino acid to see what is our first AA, we then grab the pKa value for the alpha  amine (object 4 in each nested list).
    if lastAA.count(possibleAA[i][0]) != 0:
        pKaList.append(possibleAA[i][3])  # doing a similar job but instead appending the terminal alpha carboxylic acid to the pKalist variable.
for i in range(len(RgroupWpKa)):   # for each of the potentially positive or negative R groups, do something.
    if uAAchain.count(RgroupWpKa[i][0]) != 0:  # If you find that we have one of those special AA's, do something.

        for k in range( (uAAchain.count(RgroupWpKa[i][0]))): #for each one of that kind that you find..
            pKaList.append(RgroupWpKa[i][1])                 # add it's R group's pKa to the list of pKa's
print('\nThis is the unsorted pKa list:')   # that new line looking nice!
print(pKaList)
sortList = sorted(pKaList)  # new variable that will just hold the list, we must do this as we cant do sorted(pKaList)[n] where n indexes.
print("\nThis is the sorted list of pKa's:")
print(sorted(pKaList))


Isoelectronic_point = (sortList[Max_charge-1] + sortList[Max_charge])/2   # pretty explanatory, but given that the max charge is defined as the distance from zero, we can use it to find the zero point.
                                                                          # REMEMBER THAT INDEX STARTS AT 0 AND MAX CHARGE STARTS COUNTING AT ONE, this is why I used ([n-1] + [n])/2

print('\nThe isoelectronic point of this AA chain is: ' + str(Isoelectronic_point))