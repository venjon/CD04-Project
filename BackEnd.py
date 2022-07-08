def fillstring(initial,full_len):
	charsLeft=full_len - len(initial)
	finalstring=""
	for i in range(charsLeft):
		finalstring += " "
	finalstring += initial
	return finalstring

TITLE = "Testing"
MAT = "RESER"
NAD = ""
DROK = "2650."
POR = ".01"
PER1 = "6.E-13"
PER2 = "6.E-13"
PER3 = "6.E-13"
CWET = "2.1"
SPHT = "1000."
rockline="ROCKS----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"


rock_elements = [TITLE, MAT, NAD, DROK, POR, PER1, PER2, PER3, CWET, SPHT]

def addrocks(elements):
	for i in range(len(elements)):
		if i==0:
			print(elements[i])
			print(rockline)
		elif i==1 or i==2:
			print(fillstring(elements[i],5), end="")
		else:
			print(fillstring(elements[i],10), end="")

addrocks(rock_elements)
print()

	
	

	
