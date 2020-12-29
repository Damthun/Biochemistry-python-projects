# Write a program that performs the following actions:
# - Asks the user to enter the name of an amino acid.
# - Report to the user whether that amino acid has an aliphatic, aromatic, acidic, basic, hydroxylic, sulfurcontaining, or amidic character. Use this chart as a reference when you’re creating your program! For full credit,
# you MUST use at least one logical operator in your code somewhere!
# - Make your program accept answers in a case-insensitive manner (in other words, the name can be entered
# regardless of capitalization).
# - Display a custom message letting the user know if they typed in something other than an amino acid name.

a = ['apples', 'apples']
Count = a.count("Apples")
print(Count)


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

AminoA = input("What amino acid we goin' with today?  \n")

ValidAA = listAmino.count(AminoA)
if ValidAA == 0:
    print("This is not a valid Amino acid, Try again!")
else:
    print("Great! Let's find what categories this thing fits into! \n")
    lis = []
    check = []
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



if Check < 8 and Check > 6:
    print('Your amino acid, ' + AminoA + " does not fit into our categories. Although that's a pretty cool name!")
else:
   print('Your amino acid, ' + AminoA + ' is: ' +str(lis[0]))