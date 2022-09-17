import matplotlib.pyplot as plt
from Buildings import *

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
    'CMat' : 0,
    'AMat1' : 0,
    'AMat2' : 0,
    'AMat3' : 0,
    'AMat4' : 0,
    'AMat5' : 0,
    'SandBag' : 0,
    'BarbWire' : 0,
    'PCMat' : 0,
    'Pipe' : 0,
    'MetalBeam' : 0,
    'SCMat' : 0,
    'EMat' : 0,
    'HEMat' : 0,
    'FlameAmmo' : 0,
    '250mm' : 0,
    '75mm' : 0,
    '94.5mm' : 0,
    '120mm' : 0,
    '150mm' : 0,
    '300mm' : 0,
    'HERockets' : 0,
    'FireRocket' : 0,
}

# Start
duration = int(input('\nHow many seconds for the simulation ? '))
factories = []
powerplants = []

answer = 'x'
while answer != 's':
    answer = input('\nDo you want to add a building or resources or start the simulation ? (b/r/s) ')
    if answer == 'b':
        answer = input('Enter a building number : (0:OilWell, 1:WaterPump, 2:CoalRefinery, 3:OilRafinery, 4:MetalworksFactory, 5:AmmunitionFactory, 6:DieselPowerPlant, 7:PowerStation) ')
        if answer == '0' : 
            factories.append(OilWell())
        elif answer == '1' :
            factories.append(WaterPump())
        elif answer == '2' :
            factories.append(CoalRefinery())
        elif answer == '3' :
            factories.append(OilRafinery())
        elif answer == '4' :
            factories.append(MetalworksFactory())
        elif answer == '5' :
            factories.append(AmmunitionFactory())
        elif answer == '6' :
            powerplants.append(DieselPowerPlant())
        elif answer == '7' :
            powerplants.append(PowerStation())
        
    if answer == 'r':
        print('\nResources are actually :')
        print(Res)
        mat,num = input('Type the exact name and the amount separated by a space : ').split()
        Res[mat] += int(num)

# Init Display
DispRes = [[value] for key,value in Res.items()]
ListElec = [0]

# Updates
for t in range(1,duration+1):
    EPower = 0
    for pp in powerplants:
        for pp in pp.processes:
            if pp[0]>0:
                pp[0] += 1
            if pp[0] == 0:
                canBeStarted = True
                for rr in pp[1]:
                    if Res[rr[0]] < rr[1]:
                        canBeStarted = False
                if canBeStarted == True:
                    for rr in pp[1]:
                        Res[rr[0]] -= rr[1]
                    pp[0] = 1
            if pp[0] == pp[3]:
                EPower += pp[2]
                pp[0] = 0
                for rr in pp[4]:
                    Res[rr[0]] += rr[1]
            if pp[0] != 0:
                EPower += pp[2]
            #print(pp)
        
    for ff in factories:
        for pp in ff.processes:
            if pp[0]>0:
                if EPower >= pp[2]:
                    pp[0] += 1
                    EPower -= pp[2]
            if pp[0] == 0:
                canBeStarted = True
                for rr in pp[1]:
                    if Res[rr[0]] < rr[1]:
                        canBeStarted = False
                if canBeStarted == True and EPower >= pp[2]:
                    for rr in pp[1]:
                        Res[rr[0]] -= rr[1]
                    pp[0] = 1
                    EPower -= pp[2]
            if pp[0] == pp[4]:
                pp[0] = 0
                for rr in pp[3]:
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