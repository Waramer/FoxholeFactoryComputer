# FACTORIES
#[Usage,timer,[inputs],[PowerNeeded],[outputs],duration]
class OilWell:
    def __init__(self):
        upgrade = input("\nYou are creating an OilWell, which upgrade do you wish? (0:None, 1:ElectricalOilWell, 2:Fracker) ")
        self.processes = []
        pp0=[False,0,[],0,[['Oil',1]],50]
        if usageFactory(pp0) : self.processes.append(pp0)
        if upgrade=='1':
            pp1 = [False,0,[],2,[['Oil',1]],26]
            if usageFactory(pp1) : self.processes.append(pp1)
            pp2 = [False,0,[],2,[['LOil',75]],40]
            if usageFactory(pp2) : self.processes.append(pp2) 
        elif upgrade=='2':
            pp3 = [False,0,[['LWater',25]],3,[['Oil',2]],40]
            if usageFactory(pp3) : self.processes.append(pp3)
            pp4 = [False,0,[['LWater',25]],3,[['LOil',75]],30]
            if usageFactory(pp4) : self.processes.append(pp4)

class CoalRefinery:
    def __init__(self):
        upgrade = input("\nYou are creating an CoalRafinery, which upgrade do you wish ? (0:None, 1:CokeFurnace, 2:CoalLiquifier, 3:AdvancedCoalLiquifier) ")
        self.processes = []
        pp0 = [False,0,[['Coal',200]],3,[['Coke',180]],120]
        if usageFactory(pp0) : self.processes.append(pp0)
        if upgrade=='1':
            pp1 = [False,0,[['Coal',200]],3,[['Coke',165],['Sulfur',15]],120]
            if usageFactory(pp1) : self.processes.append(pp1)
        elif upgrade=='2':
            pp2 = [False,0,[['Coal',300],['LWater',75]],4,[['Concrete',180],['LOil',50]],120]
            if usageFactory(pp2) : self.processes.append(pp2)
        elif upgrade=='3':
            pp3 = [False,0,[['Coal',300],['LWater',150]],4,[['Coke',260],['LHOil',60]],180]
            if usageFactory(pp3) : self.processes.append(pp3)

# POWER PLANTS
class DieselPowerPlant:
    def __init__(self):
        upgrade = input("\nYou are creating an DieselPowerPlant, which upgrade do you wish ? (0:None, 1:PetrolPowerPlant) ")
        self.processes = []
        pp0 = [False,0,[['LDiesel',25]],5,45]
        if usagePlant(pp0) :self.processes.append(pp0)
        if upgrade=='1':
            pp1 = [False,0,[['LPetrol',50]],12,90]
            if usagePlant(pp1) : self.processes.append(pp1)

# TOOL FUNCTIONS
def usageFactory(pp):
    print('Do you want to use the process : ',end='')
    for rr in pp[2] : print(str(rr[1])+rr[0],end='')
    print(' -> ',end='')
    for rr in pp[4] : print(str(rr[1])+rr[0],end='')
    use = input('('+str(pp[5])+'s '+str(pp[3])+'MW) ? (y/n) ')
    if use == 'y' : pp[0] = True
    return use

def usagePlant(pp):
    print('Do you want to use the process : ',end='')
    for rr in pp[2] : print(str(rr[1])+rr[0],end='')
    print(' -> '+str(pp[3])+'MW',end='')
    use = input('('+str(pp[4])+'s) ? (y/n) ')
    if use == 'y' : pp[0] = True
    return use