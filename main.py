import numpy as np
import matplotlib.pyplot as plt
from Buildings import *

#======== Main Beginning ========

# ==== Asking which type of analysis is wanted ====
# analysistype = input("Which simulation do you want to perform ? ")

# ==== Type 1 Simulation ====
Res = {
    'LDiesel' : 0,
    'Oil' : 0,
    'LOil' : 0,
    'HOil' : 0,
    'LHOil' : 0,
    'EOil' : 0,
    'LEOil' : 0,
    'Water' : 0,
    'LWater' : 0,
    'Coal' : 0,
    'Coke' : 0,
    'Sulfur' : 0,
    'Concrete' : 0,
    'Petrol' : 0,
    'LPetrol' : 0,
}

# Init Display
DispRes = [[value] for key,value in Res.items()]
ListElec = [0]

# Start
duration = int(input('\nHow many seconds for the simulation ? '))
factories = []
powerplants = []

answer = 'x'
while answer != 's':
    answer = input('\nDo you want to add a building or resources or start the simulation ? (b/r/s) ')
    if answer == 'b':
        answer = input('Enter a building number : (0:OilWell, 1:CoalRefinery, 2:DieselPowerPlant) ')
        if answer == '0' : 
            oilwell = OilWell()
            factories.append(oilwell)
        if answer == '1' :
            coalrafinery = CoalRefinery()
            factories.append(coalrafinery)
        if answer == '2' :
            dieselpowerplant = DieselPowerPlant()
            powerplants.append(dieselpowerplant)
        
    if answer == 'r':
        print('\nResources are actually :')
        print(Res)
        mat,num = input('Type the exact name and the amount separated by a space : ').split()
        Res[mat] += int(num)

# Updates
for t in range(1,duration+1):
    EPower = 0
    for pp in powerplants:
        for pp in pp.processes:
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
                if pp[1] == pp[4]:
                    EPower += pp[3]
                    pp[1] = 0
                if pp[1] != 0:
                    EPower += pp[3]
            #print(pp)
        
    for ff in factories:
        for pp in ff.processes:
            if pp[0] == True:
                if pp[1]>0:
                    if EPower >= pp[3]:
                        pp[1] += 1
                        EPower -= pp[3]
                if pp[1] == 0:
                    canBeStarted = True
                    for rr in pp[2]:
                        if Res[rr[0]] < rr[1]:
                            canBeStarted = False
                    if canBeStarted == True and EPower >= pp[3]:
                        for rr in pp[2]:
                            Res[rr[0]] -= rr[1]
                        pp[1] = 1
                        EPower -= pp[3]
                if pp[1] == pp[5]:
                    pp[1] = 0
                    for rr in pp [4]:
                        Res[rr[0]] += rr[1]
            #print(pp)

    #print(str(t)+' : Res:'+str(Res)+'  Elec:'+str(EPower))
    #Update Display Lists
    i=0
    for key,value in Res.items():
        DispRes[i].append(value)
        i += 1
    ListElec.append(EPower)

# End of Simulation
print('\nRes:'+str(Res)+'  Elec:'+str(EPower))

# Display
fig,(ax1,ax2,ax3) = plt.subplots(3)

i=0
for key,value in Res.items():
    if key[0] == 'L':
        ax2.plot(range(0,duration+1),DispRes[i],label=key)
    else:
        ax1.plot(range(0,duration+1),DispRes[i],label=key)
    i += 1

ax1.grid()
ax1.legend()
ax2.grid()
ax2.legend()
ax3.plot(range(0,duration+1),ListElec,label='ElectricPower')
ax3.grid()
ax3.legend()
plt.show()

