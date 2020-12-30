

#This exercised used python lists and if/else loops to determine whether an amino acid entered by the user belongs to a series of categories.
#If the amino acid belongs in any of these lists the program will print the category it fits into.

#So during this project I wasn't supposed to use dictionaries so that affects the opportunity to be concise.
listAmino = ["alanine",'Alanine', 'Arginine', 'arginine', 'asparagine', 'Asparagine', 'Aspartate', 'aspartate', 'Cysteine', 'cysteine', 'Glutamine', 'glutamine', 'Glutamate', 'glutamate', 'glycine', 'Glycine', 'Histidine', 'histidine', 'Isoleucine', 'isoleucine', 'Leucine',
             'leucine', 'Lysine', 'lysine', 'Methionine', 'methionine', 'Phenylalanine', 'phenylalanine', 'Proline', 'proline', 'Serine', 'serine', 'Threonine', 'threonine'
             , 'Tryptophan', 'tryptophan', 'Tyrosine', 'tyrosine', 'Valine', 'valine', 'Binderine', 'binderine']
Aliphatic = ["Isoleucine", "isoleucine", 'Valine', 'valine', 'Leucine', 'leucine', 'Alanine', 'alanine', 'Proline', 'proline', 'Glycine', 'glycine']
Aromatic = ['Tyrosine', 'tyrosine', 'Tryptophan', 'tryptophan', 'Phenylalanine', 'phenylalanine']
Acidic = ['Aspartate', 'aspartate', 'Glutamate', 'glutamate']
Basic = ['Arginine', 'arginine', 'Lysine', 'lysine', 'Histidine', 'histidine']
Hydroxylic = ['Serine', 'serine', 'Threonine', 'threonine']
Sulfur = ['methionine', 'Methionine', 'Cysteine', 'cysteine', 'Homocysteine', 'homocysteine', 'Taurine', 'taurine']
Amidic = ['Asparagine', 'asparagine', 'glutamine', 'Glutamine']


AminoA = input("What amino acid we goin' with today?  \n") # user inputs the name of an amino acid.

ValidAA = listAmino.count(AminoA) #A variable that checks if the input is an amino acid.
if ValidAA == 0:                  # if the count results in zero (the AA isn't in the list), tell the user it's not valid.
    print("This is not a valid Amino acid, Try again!")
else:
    print("Great! Let's find what categories this thing fits into! \n") 
    lis = []                                    #Creating two lists, one that describes the Amino Acid and one that notes if the condition isn't met.
    check = []                                  #This approach wouldn't work if the AA were allotted the ability to be in more than one category.
    if Aliphatic.count(AminoA) ==1:
        lis.append('Aliphatic')
    else: check.append(0)

    if Aromatic.count(AminoA) ==1:
        lis.append('Aromatic')
    else:check.append(0)

    if Acidic.count(AminoA) ==1:
        lis.append('Acidic')
    else:check.append(0)

    if Basic.count(AminoA) ==1:
        lis.append('Basic')
    else:check.append(0)0

    if Hydroxylic.count(AminoA) ==1:
        lis.append('Hydroxylic')
    else:check.append(0)

    if Sulfur.count(AminoA) ==1:
        lis.append('Sulfur-containing')
    else:check.append(0)

    if Amidic.count(AminoA) ==1:
        lis.append('Amidic')
    else: check.append(0)

Check = check.count(0) 



if Check < 8 and Check > 6:  #This could be used by doing if Check == 7: but the prompt requested a logical operator!
    print('Your amino acid, ' + AminoA + " does not fit into our categories. Although that's a pretty cool name!")
else:
   print('Your amino acid, ' + AminoA + ' is: ' +str(lis[0]))  #Note, I knew that the lis variable would only have one str so I used str(lis[0]). 
                                                               #If there was more than one possible option I would have used a print statement for the "your amino acid is:"
                                                               #And then use a conditional statement in conjunction with the new line \n functionality to print them in a column format.
    
