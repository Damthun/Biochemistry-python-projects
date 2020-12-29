##Copy your program from the first exercise, and add the following functionality:
#Display the original sequence for the user at the start of the session, all in uppercase.
#Allow the user to specify where the substitution will start and end.
#Allow the user to specify the sequence that will be substituted.
#Display the altered sequence using the same uppercase/lowercase convention from the first exercise

seQ = "aatcgcgattagtcatgaaaat"
seQ2 = seQ.upper()

print("The current sequence is :"+ seQ2)
start = input('What value does your change start at? (note that indexing starts at zero)')
end = input('What value does your change end at?')
replacement = input("what is the new sequence you'd like to be input?")
newSeq = seQ2.replace(seQ2[int(start):int(end)], replacement.lower())

print(newSeq)
