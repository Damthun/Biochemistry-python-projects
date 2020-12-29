# This exercise takes the functionality of the first exercise, but adds the ability to choose what section of the sequence to replace with a new user-defined section.
seQ = "aatcgcgattagtcatgaaaat" # initial sequence
seQ2 = seQ.upper() #making the sequence uppercase, Just a preference for me.

print("The current sequence is :"+ seQ2)
start = input('What value does your change start at? (note that indexing starts at zero)') # prompts the user to pick where they'd like to start their splice.
end = input('What value does your change end at?') #prompts the user to pick an end point for their splice.
replacement = input("what is the new sequence you'd like to be input?") #prompts the user to pick their insert.
newSeq = seQ2.replace(seQ2[int(start):int(end)], replacement.lower()) #creates a new variable that stores the new sequence by replacing the user given range with the given insert.

print(newSeq)
