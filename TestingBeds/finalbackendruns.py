from COFT.COFTmerge import addCOFT
from DIFFU.DIFFUmerge import addDiffu
from FINAL.FinalMergeVennela import addFOFT, addGOFT, addTimes, addindom, addmulti, addparam, addselec, addsolvr

def checkfull(listname):
  for x in range(len(listname)):
    if listname[x]!="":
        return True
  return False

if(checkfull(multi)):
  addmulti()

if(checkfull(coft)):
  addCOFT()

if(checkfull(diffu)):
  addDiffu()

if(checkfull(foft)):
  addFOFT()

if(checkfull(goft)):
  addGOFT()
  
if(checkfull(param)):
  addparam()
  
if(checkfull(selec)):
  addselec()
  
if(checkfull(solvr)):
  addsolvr()

if(checkfull(times)):
  addTimes()

if(checkfull(indom)):
  addindom()
