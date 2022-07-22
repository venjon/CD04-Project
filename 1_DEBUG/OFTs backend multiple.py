def checkexists(examplestring):
    if (examplestring=="" or examplestring=="separate by commas"):
        return False
    return True
    
def addFOFT():
    FOFTline="FOFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write(FOFTline) 
    if(checkexists(EOFT1.get()):   
        f.write(fillstring(EOFT1.get(),5)+"\n")
    if(checkexists(EOFT2.get()):
        f.write(fillstring(EOFT2.get(),5)+"\n")
    if(checkexists(EOFT3.get()):
        f.write(fillstring(EOFT3.get(),5)+"\n")
    if(checkexists(EOFT4.get()):
        f.write(fillstring(EOFT4.get(),5)+"\n")
    if(checkexists(EOFT5.get()):
        f.write(fillstring(EOFT5.get(),5)+"\n")
    if(checkexists(EOFT6.get()):
        f.write(fillstring(EOFT6.get(),5)+"\n")
    if(checkexists(EOFT7.get()):
        f.write(fillstring(EOFT7.get(),5)+"\n")
    if(checkexists(EOFT8.get()):
        f.write(fillstring(EOFT8.get(),5)+"\n")
    if(checkexists(EOFT9.get()):
        curnum=0
        curstring=""
        for i in range(len(EOFT9.get())):
            if(EOFT9.get()[i]==','):
                curstring=fillstring(curstring,5)
                f.write(curstring)
                curstring=""
            else:
                curstring+=EOFT9.get()[i]
        f.write(fillstring(curstring,5)+"\n")
    


def addCOFT():
    COFTline="COFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write(COFTline)    
    if(checkexists(ECOFT1.get()): 
        f.write(fillstring(ECOFT1.get(),5)+"\n")
    if(checkexists(ECOFT2.get()):
        f.write(fillstring(ECOFT2.get(),5)+"\n")
    if(checkexists(ECOFT3.get()):
        f.write(fillstring(ECOFT3.get(),5)+"\n")
    if(checkexists(ECOFT4.get()):
        f.write(fillstring(ECOFT4.get(),5)+"\n")
    if(checkexists(ECOFT5.get()):
        f.write(fillstring(ECOFT5.get(),5)+"\n")
    if(checkexists(ECOFT6.get()):
        f.write(fillstring(ECOFT6.get(),5)+"\n")
    if(checkexists(ECOFT7.get()):
        f.write(fillstring(ECOFT7.get(),5)+"\n")
    if(checkexists(ECOFT8.get()):
        f.write(fillstring(ECOFT8.get(),5)+"\n")
    if(checkexists(ECOFT9.get()):
        curnum=0
        curstring=""
        for i in range(0,len(ECOFT9.get()):
            if(ECOFT9.get()[i]==','):
                curstring=fillstring(curstring,5)
                f.write(curstring)
                curstring=""
            else:
                curstring+=ECOFT9.get()[i]
        f.write(fillstring(curstring,5)+"\n")
    

def addGOFT():
    GOFTline="GOFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write(GOFTline)    
    if(checkexists(EGOFT1.get()): 
        f.write(fillstring(EGOFT1.get(),5)+"\n")
    if(checkexists(EGOFT2.get()):
        f.write(fillstring(EGOFT2.get(),5)+"\n")
    if(checkexists(EGOFT3.get()):
        f.write(fillstring(EGOFT3.get(),5)+"\n")
    if(checkexists(EGOFT4.get()):
        f.write(fillstring(EGOFT4.get(),5)+"\n")
    if(checkexists(EGOFT5.get()):
        f.write(fillstring(EGOFT5.get(),5)+"\n")
    if(checkexists(EGOFT6.get()):
        f.write(fillstring(EGOFT6.get(),5)+"\n")
    if(checkexists(EGOFT7.get()):
        f.write(fillstring(EGOFT7.get(),5)+"\n")
    if(checkexists(EGOFT8.get()):
        f.write(fillstring(EGOFT8.get(),5)+"\n")
    if(checkexists(EGOFT9.get()):
        curnum=0
        curstring=""
        for i in range(0,len(EGOFT9.get())):
            if(EGOFT9.get()[i]==','):
                curstring=fillstring(curstring,5)
                f.write(curstring)
                curstring=""
            else:
                curstring+=EGOFT9.get()[i]
        f.write(fillstring(curstring,5)+"\n")
    


def addFOFT():
    FOFTline="FOFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write(FOFTline+"\n")    
    f.write(fillstring(EOFT.get(),5) )
    f.write("\n")


def addCOFT():
    COFTline="COFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write(COFTline+"\n")    
    f.write(fillstring(ECOFT.get(),10) )
    f.write("\n")

def addGOFT():
    GOFTline="GOFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write(GOFTline+"\n")    
    f.write(fillstring(EGOFT.get(),5) )
    f.write("\n")
    
    
    