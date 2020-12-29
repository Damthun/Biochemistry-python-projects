# Exercise #4:
# Write a program that performs the following actions:
# - Asks the user to enter a sequence of one-letter amino acid codes (see this chart).
# - Display the same sequence as a list of three-letter amino acid codes separated by dashes. For example, if the
# user enters “GGLYS”, the output of your program should be “Gly-Gly-Leu-Tyr-Ser”. For full credit, you must
# employ a “for” loop somewhere in your code

Sequence = input("What's that amino acid sequence?         (NOTE: IF YOU PICK A LETTER THAT DOESNT CORRESPOND TO AN AA IT WILL BE OMITTED!\n")

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



#print(newseq)
newseq2 = '-'.join(newseq)
print('Your sequence of amino acids is \n'  + newseq2 + '.')