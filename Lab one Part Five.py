# Write a program that displays the complementary sequence for a DNA sequence entered by the user. Again, for full
#credit, you must employ a “for” loop somewhere in your code

NSeq = input('I heard you have DNA, How many strings ya got?')
nonATCG = 'bdefhijklmnopqrsuvwxyz'
for i in range((int(NSeq))):
    if i == 0:
        Sequence = input('I heard you have DNA, ENTER Sequence here:')
        Sequence2 = Sequence.lower()
        T = Sequence2.replace('t', 'A')
        A = T.replace('a', 'T')
        G = A.replace('g', 'C')
        C = G.replace('c', 'G')
        for char in nonATCG:
            C = C.replace(char, "")
        print("The complementary string is: \n" + C)
    elif i == 1:
        Sequence = input("Keep them comin':")
        Sequence2 = Sequence.lower()
        T = Sequence2.replace('t', 'A')
        A = T.replace('a', 'T')
        G = A.replace('g', 'C')
        C = G.replace('c', 'G')
        for char in nonATCG:
            C = C.replace(char, "")
        print("The complementary string is: \n" + C)
    elif i == 2:
        Sequence = input("Wow, you've got lots of strands! ENTER:")
        Sequence2 = Sequence.lower()
        T = Sequence2.replace('t', 'A')
        A = T.replace('a', 'T')
        G = A.replace('g', 'C')
        C = G.replace('c', 'G')
        for char in nonATCG:
            C = C.replace(char, "")
        print("The complementary string is: \n" + C)
    elif i == 3:
        Sequence = input("Now you're just playing with me! I am a computer though so I have to allow it, What's the string?")
        Sequence2 = Sequence.lower()
        T = Sequence2.replace('t', 'A')
        A = T.replace('a', 'T')
        G = A.replace('g', 'C')
        C = G.replace('c', 'G')
        for char in nonATCG:
            C = C.replace(char, "")
        print("The complementary string is: \n" + C)

    else:
        Sequence = input(".....")
        Sequence2 = Sequence.lower()
        T = Sequence2.replace('t', 'A')
        A = T.replace('a', 'T')
        G = A.replace('g', 'C')
        C = G.replace('c', 'G')
        for char in nonATCG:
            C = C.replace(char, "")
        print(C)
