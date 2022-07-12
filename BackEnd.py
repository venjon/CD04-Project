def fillstring(initial,full_len):
	charsLeft=full_len - len(initial)
	finalstring=""
	if charsLeft < 0:
		for i in range(5):
			finalstring+=initial[i]
	for i in range(charsLeft):
		finalstring+=" "
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
COM=""
EXPAN=""
CDRY=""
TORTX="" 
GK="" 
XKD3=""
XKD3="" 
XKD4="" 
IRP=""
RP1=""
RP2=""
RP3="" 
RP4="" 
RP5="" 
RP6="" 
RP7=""
ICP="67098"
CP1=""
CP2=""
CP3=""
CP4=""
CP5=""
CP6=""
CP7=""
rockline="ROCKS----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"

rock_elements = [TITLE, MAT, NAD, DROK, POR, PER1, PER2, PER3, CWET, SPHT,COM, EXPAN, CDRY, TORTX, GK, XKD3, XKD3, XKD4, IRP, RP1, RP2,RP3, RP4, RP5, RP6, RP7, ICP, CP1, CP2, CP3, CP4, CP5, CP6, CP7]

def addrocks(elements):
	for i in range(len(elements)):
		if i==0:
			print(elements[i])
			print(rockline)
		elif i==1 or i==2:
			print(fillstring(elements[i],5), end="")
		elif i<=9:
			print(fillstring(elements[i],10), end="")
		elif i<=10:
			print()
			print(fillstring(elements[i],10), end="")
		elif i<=16:
			print(fillstring(elements[i],10), end="")
		elif i<=17:
			print()
			print(fillstring("",5), end="")
		elif i<=18:
			print(fillstring("",5), end ="")
			print(fillstring(elements[i],10), end="")
		elif i<=24:
			print(fillstring("",10), end="")
		elif i<=25:
			print()
			print(fillstring("",5), end="")
		elif(i<=26):
			print(fillstring("",5), end ="")
			print(fillstring(elements[i],10), end="")
		elif(i<=32):
			print(fillstring(elements[i],10), end="")		
	print()

addrocks(rock_elements)


	
	

	
