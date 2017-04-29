
list_ini=["NDA","MLP","MAC","HAM","ART","POU","CHE","LAS","MEL","ASS","FIL","SUP"]

num_case=list(range(4,17))
print(num_case)
i=0
donnees={}
for nom in list_ini:
	int_val="val_mac"+nom
	int_form="abs_"+nom
	num=str(num_case[i])
	print(num)
	donnees["H"+num]=2
	i += 1
print(donnees)
