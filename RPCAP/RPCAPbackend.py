#get from rocks

#backend RPCAP

def addrpcap(elements):
    rpcapline="RPCAP----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print (rpcapline)
    print (fillstring(elements[17],5),end="")
    print(fillstring("",5), end ="")
    print (fillstring(elements[18],10),end="")
    print (fillstring(elements[19],10),end="")
    print (fillstring(elements[20],10),end="")
    print (fillstring(elements[21],10),end="")
    print (fillstring(elements[22],10),end="")
    print (fillstring(elements[23],10),end="")
    print (fillstring(elements[24],10),end="")
    print()
    print (fillstring(elements[25],5),end="")
    print(fillstring("",5), end ="")
    print (fillstring(elements[26],10),end="")
    print (fillstring(elements[27],10),end="")
    print (fillstring(elements[28],10),end="")
    print (fillstring(elements[29],10),end="")
    print (fillstring(elements[30],10),end="")
    print (fillstring(elements[31],10),end="")
    print (fillstring(elements[32],10),end="")
    print()
        
        
for key in rockDict:
  dummy = rockDict[key]
  addrocks(dummy)
