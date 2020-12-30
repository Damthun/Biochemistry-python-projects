
#This exercise takes a user defined dna sequence and outputs the complementary sequence by use of a for loop.

NSeq = input('I heard you have DNA, How many strings ya got?')
nonATCG = 'bdefhijklmnopqrsuvwxyz' # These are the letters that aren't deoxy-nucleotides.
for i in range((int(NSeq))):  # iterate through the number of sequences given.
    if i == 0:                # for the first sequence...
        Sequence = input('I heard you have DNA, ENTER Sequence here:') #input the sequence
        Sequence2 = Sequence.lower()                                   #Make the sequence lowercase, user proofing as much as i can.
        T = Sequence2.replace('t', 'A')                                ## Here I am replacing the lowercase of a nucleotide with an uppercase, this is so that I dont replace
        A = T.replace('a', 'T')                                        ## something that is already replaced i.e. agt ->agA ->TgA ->TCA NOT agt > aga > tgt
        G = A.replace('g', 'C')
        C = G.replace('c', 'G')
        for char in nonATCG:                    #Back to user proofing. If there is a non deoxy nucleotide such as z,b,k,l etc. replace it with nothing.
            C = C.replace(char, "")             # So it's checking b, then d, then e etc. and if there is a non deoxy nucleotide its updating the variable c.
        print("The complementary string is: \n" + C)
    elif i == 1:  # Do the same stuff but for the second sequence...
        Sequence = input("Keep them comin':") #giving it a bit of life.
        Sequence2 = Sequence.lower()
        T = Sequence2.replace('t', 'A')
        A = T.replace('a', 'T')
        G = A.replace('g', 'C')
        C = G.replace('c', 'G')
        for char in nonATCG:
            C = C.replace(char, "")
        print("The complementary string is: \n" + C)
    elif i == 2:
        Sequence = input("Wow, you've got lots of strands! ENTER:") # just a bit of humor.
        Sequence2 = Sequence.lower()
        T = Sequence2.replace('t', 'A')
        A = T.replace('a', 'T')
        G = A.replace('g', 'C')
        C = G.replace('c', 'G')
        for char in nonATCG:
            C = C.replace(char, "")
        print("The complementary string is: \n" + C)
    elif i == 3:
        Sequence = input("Now you're just playing with me! I am a computer though so I have to allow it, What's the string?") #more humor.
        Sequence2 = Sequence.lower()
        T = Sequence2.replace('t', 'A')
        A = T.replace('a', 'T')
        G = A.replace('g', 'C')
        C = G.replace('c', 'G')
        for char in nonATCG:
            C = C.replace(char, "")
        print("The complementary string is: \n" + C)

    else:
        Sequence = input(".....") # I suppose the computer got tired of it.
        Sequence2 = Sequence.lower()
        T = Sequence2.replace('t', 'A')
        A = T.replace('a', 'T')
        G = A.replace('g', 'C')
        C = G.replace('c', 'G')
        for char in nonATCG:
            C = C.replace(char, "")
        print(C)
