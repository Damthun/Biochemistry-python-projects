seQ = "aatcgcgattagtcatgaaaat"
SeQvariant = seQ.replace('gattag', 'gagaga' )
SeQvariant= SeQvariant.upper()


#print(SeQvariant)

# Screw it, Ill start with SeQ being upper, easier than rewriting.

seQ2 = seQ.upper()
seQvariant2 = seQ2.replace('GATTAG', 'gagaga')
print(seQvariant2)