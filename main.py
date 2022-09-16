import numpy
import matplotlib.pyplot
from Buildings import *

#======== Main Beginning ========

# ==== Asking which type of analysis is wanted ====
# analysistype = input("Which simulation do you want to perform ? ")

# ==== Type 1 Simulation ====
Res = {
    'Oil' : 0,
    'LOil' : 0,
    'Water' : 0,
    'LWater' : 0,
}
EPower = 0

class OilWell:
    def __init__(self,upgrade):
        self.nbProcess = [1,3,3]
        self.processes = [[True,0,[],0,[['Oil',1]],50]]
        if upgrade==1:
            self.processes.append([False,0,[],2,[['Oil',1]],26])
            self.processes.append([False,0,[],2,[['LOil',75]],40]) 
        if upgrade==2:
            self.processes.append([False,0,[['LWater',25]],3,[['Oil',2]],40])
            self.processes.append([False,0,[['LWater',25]],3,[['LOil',75]],30])


duration = 110
factories = [OilWell(0)]

# Start

# Updates
for t in range(1,duration+1):
    for ff in factories:
        for pp in ff.processes:
            if pp[0] == True:
                if pp[1]>0:
                    pp[1] += 1
                if pp[1] == 0:
                    canBeStarted = True
                    for rr in pp[2]:
                        if Res[rr[0]] < rr[1]:
                            canBeStarted = False
                    if canBeStarted == True:
                        for rr in pp[2]:
                            Res[rr[0]] -= rr[1]
                        pp[1] = 1   
                if pp[1] == pp[5]:
                    pp[1] = 0
                    for rr in pp [4]:
                        Res[rr[0]] += rr[1]
            print(pp)
    print(str(t)+' : '+str(Res))

