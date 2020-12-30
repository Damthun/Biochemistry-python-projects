#This exercise required me to have the user enter an amino acid sequence and output the sequence in three letter format i.e. G -> Gly.
Sequence = input("What's that amino acid sequence?         (NOTE: IF YOU PICK A LETTER THAT DOESNT CORRESPOND TO AN AA IT WILL BE OMITTED!\n")

#the premise behind the functionality is to make a list, and use a for loop to iterate through each letter in the sequence to append the three letter code in order.
newseq=[]

for i in range(len(Sequence)):
     if Sequence[i] == 'G' or Sequence[i] == 'g':
         newseq.append('Gly')
     elif Sequence[i] == 'P' or Sequence[i] == 'p':
        newseq.append('Pro')
     elif Sequence[i] == 'V' or Sequence[i] == 'v':
        newseq.append('Val')
     elif Sequence[i] == 'H' or Sequence[i] == 'h':
        newseq.append('His')
     elif Sequence[i] == 'R' or Sequence[i] == 'r':
        newseq.append('Arg')
     elif Sequence[i] == 'E' or Sequence[i] == 'e':
        newseq.append('Glu')
     elif Sequence[i] == 'L' or Sequence[i] == 'l':
        newseq.append('Leu')
     elif Sequence[i] == 'F' or Sequence[i] == 'f':
        newseq.append('Phe')
     elif Sequence[i] == 'D' or Sequence[i] == 'd':
        newseq.append('Asp')
     elif Sequence[i] == 'I' or Sequence[i] == 'i':
        newseq.append('Ile')
     elif Sequence[i] == 'M' or Sequence[i] == 'm':
        newseq.append('Met')
     elif Sequence[i] == 'C' or Sequence[i] == 'c':
        newseq.append('Cys')
     elif Sequence[i] == 'T' or Sequence[i] == 't':
        newseq.append('Thr')
     elif Sequence[i] == 'Y' or Sequence[i] == 'y':
        newseq.append('Tyr')
     elif Sequence[i] == 'W' or Sequence[i] == 'w':
        newseq.append('Trp')
     elif Sequence[i] == 'S' or Sequence[i] == 's':
        newseq.append('Ser')
     elif Sequence[i] == 'K' or Sequence[i] == 'k':
        newseq.append('Lys')
     elif Sequence[i] == 'A' or Sequence[i] == 'a':
        newseq.append('Ala')
     elif Sequence[i] == 'Q' or Sequence[i] == 'q':
        newseq.append('Gln')
     elif Sequence[i] == 'N' or Sequence[i] == 'n':
        newseq.append('Asn')



newseq2 = '-'.join(newseq) # the list wouldn't be appealing if it printed as "['Gly','Leu','Asp'], So this joins them to print something more like "Gly-Leu-Asp"
print('Your sequence of amino acids is \n'  + newseq2 + '.')
