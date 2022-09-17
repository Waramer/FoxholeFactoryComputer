# HARVESTER


class OilWell:
    def __init__(self):
        upgrade = input("\nYou are creating an OilWell, which upgrade do you wish? (0:None, 1:ElectricalOilWell, 2:Fracker) ")
        self.processes = []
        pp0=[0,[],0,[['Oil',1]],50]
        if usageFactory(pp0) : self.processes.append(pp0)
        if upgrade=='1':
            pp1 = [0,[],2,[['Oil',1]],26]
            if usageFactory(pp1) : self.processes.append(pp1)
            pp2 = [0,[],2,[['LOil',75]],40]
            if usageFactory(pp2) : self.processes.append(pp2) 
        elif upgrade=='2':
            pp3 = [0,[['LWater',25]],3,[['Oil',2]],40]
            if usageFactory(pp3) : self.processes.append(pp3)
            pp4 = [0,[['LWater',25]],3,[['LOil',75]],30]
            if usageFactory(pp4) : self.processes.append(pp4)

class WaterPump:
    def __init__(self):
        upgrade = input("\nYou are creating a WaterPump, which upgrade do you wish? (0:None, 1:ElectricalWaterPump) ")
        self.processes = []
        pp0=[0,[],0,[['Water',1]],50]
        if usageFactory(pp0) : self.processes.append(pp0)
        if upgrade=='1':
            pp1=[0,[],0,[['Water',1]],40]
            if usageFactory(pp1) : self.processes.append(pp1)
            pp2=[0,[],0.5,[['LWater',60]],50]
            if usageFactory(pp2) : self.processes.append(pp2) 

# FACTORIES
class OilRafinery:
    def __init__(self):
        upgrade = input("\nYou are creating an OilRafinery, which upgrade do you wish ? (0:None, 1:Reformer+, 2:CrackingUnit, 3:PetrochimicalPlant) ")
        self.processes = []
        pp0 = [0,[['LOil',150]],1,[['LPetrol',150]],150]
        if usageFactory(pp0) : self.processes.append(pp0)
        if upgrade=='1':
            pp1 = [0,[['LOil',120],['LWater',30]],1,[['LPetrol',150]],150]
            if usageFactory(pp1) : self.processes.append(pp1)
        elif upgrade=='2':
            pp2 = [0,[['LOil',150]],1.5,[['LHOil',90]],160]
            if usageFactory(pp2) : self.processes.append(pp2)
        elif upgrade=='3':
            pp3 = [0,[['Sulfur',20],['LHOil',90]],2,[['EOil',90]],160]
            if usageFactory(pp3) : self.processes.append(pp3)

class CoalRefinery:
    def __init__(self):
        upgrade = input("\nYou are creating a CoalRafinery, which upgrade do you wish ? (0:None, 1:CokeFurnace, 2:CoalLiquifier, 3:AdvancedCoalLiquifier) ")
        self.processes = []
        pp0 = [0,[['Coal',200]],3,[['Coke',180]],120]
        if usageFactory(pp0) : self.processes.append(pp0)
        if upgrade=='1':
            pp1 = [0,[['Coal',200]],3,[['Coke',165],['Sulfur',15]],120]
            if usageFactory(pp1) : self.processes.append(pp1)
        elif upgrade=='2':
            pp2 = [0,[['Coal',300],['LWater',75]],4,[['Concrete',1],['LOil',50]],120]
            if usageFactory(pp2) : self.processes.append(pp2)
        elif upgrade=='3':
            pp3 = [0,[['Coal',300],['LWater',150]],4,[['Coke',260],['LHOil',60]],180]
            if usageFactory(pp3) : self.processes.append(pp3)

class MaterialFactory:
    def __init__(self):
        upgrade = input("\nYou are creating a MaterialFactory, which upgrade do you wish ? (0:None, 1:Forge, 2:MetalPress, 3:Smelter, 4:Recycler) ")
        self.processes = []
        pp0=[0,[['Salvage',20]],2,[['CMat',1]],25]
        if usageFactory(pp0) : self.processes.append(pp0)
        if upgrade == '1':
            pp1=[0,[['Salvage',20],['Coke',180]],2,[['AMat1',1]],60]
            if usageFactory(pp1) : self.processes.append(pp1)
            pp2=[0,[['Salvage',20],['LPetrol',150]],2,[['AMat2',1]],60]
            if usageFactory(pp2) : self.processes.append(pp2)
        if upgrade == '1':
            pp3=[0,[['Salvage',20],['LPetrol',25]],4,[['CMat',3]],25]
            if usageFactory(pp3) : self.processes.append(pp3)
        if upgrade == '1':
            pp4=[0,[['Salvage',20],['Coke',25]],4,[['CMat',3]],25]
            if usageFactory(pp4) : self.processes.append(pp4)
        if upgrade == '1':
            pp5=[0,[['Salvage',20]],2,[['CMat',1],['SandBag',5]],25]
            if usageFactory(pp5) : self.processes.append(pp5)
            pp6=[0,[['Salvage',20]],2,[['CMat',1],['BarbWire',5]],25]
            if usageFactory(pp6) : self.processes.append(pp6)

class MetalworksFactory:
    def __init__(self):
        upgrade = input("\nYou are creating a MetalworksFactory, which upgrade do you wish ? (0:None, 1:BlastFurnace, 2:Recycler, 3:EngineeringStation) ")
        self.processes = []
        pp0 = [0,[['CMat',3],['Component',20]],5,[['PCMat',1]],60]
        if usageFactory(pp0) : self.processes.append(pp0)
        pp1 = [0,[['PCMat',3]],5,[['Pipe',1]],120]
        if usageFactory(pp1) : self.processes.append(pp1)
        if upgrade == '1':
            pp2 = [0,[['CMat',3],['Component',55],['LHOil',6]],8,[['PCMat',3]],60]
            if usageFactory(pp2) : self.processes.append(pp2)
            pp3 = [0,[['PCMat',1],['LHOil',66]],5,[['AMat3',1]],120]
            if usageFactory(pp3) : self.processes.append(pp3)
            pp4 = [0,[['CMat',3],['Sulfur',20]],5,[['AMat4',1]],120]
            if usageFactory(pp4) : self.processes.append(pp4)
        if upgrade == '2':
            pp5 = [0,[['CMat',3],['Component',20]],5,[['PCMat',1],['MetalBeam',1]],60]
            if usageFactory(pp5) : self.processes.append(pp5)
            pp6 = [0,[['Salvage',200]],4,[['Component',1]],90]
            if usageFactory(pp6) : self.processes.append(pp6)
        if upgrade == '3':
            pp7 = [0,[['PCMat',3],['Component',20],['LHOil',6]],9,[['SCMat',1]],160]
            if usageFactory(pp7) : self.processes.append(pp7)
            pp8 = [0,[['PCMat',3],['Component',20],['Sulfur',20],['LHOil',3]],8,[['SCMat',3]],160]
            if usageFactory(pp8) : self.processes.append(pp8)
            pp9 = [0,[['SCMat',1],['LEOil',6]],8,[['AMat5',1]],160]
            if usageFactory(pp9) : self.processes.append(pp9)

class AmmunitionFactory:
    def __init__(self):
        upgrade = input("\nYou are creating an AmmunitionFactory, which upgrade do you wish ? (0:None, 1:LargeShellFactory, 2:RocketFactory) ")
        self.processes = []
        pp0 = [0,[['HEMat',1],['CMat',1]],4,[['FlameAmmo',1]],25]
        if usageFactory(pp0) : self.processes.append(pp0)
        pp1 = [0,[['HEMat',6],['CMat',5]],4,[['250mm',1]],30]
        if usageFactory(pp1) : self.processes.append(pp1)
        if upgrade == '1':
            pp2 = [0,[['HEMat',2],['CMat',2]],4,[['75mm',1]],25]
            if usageFactory(pp2) : self.processes.append(pp2)
            pp3 = [0,[['HEMat',2],['CMat',2]],4,[['94.5mm',1]],25]
            if usageFactory(pp3) : self.processes.append(pp3)
            pp4 = [0,[['EMat',3],['CMat',2]],4,[['120mm',1]],15]
            if usageFactory(pp4) : self.processes.append(pp4)
            pp5 = [0,[['HEMat',2],['CMat',3]],4,[['150mm',1]],20]
            if usageFactory(pp5) : self.processes.append(pp5)
            pp6 = [0,[['HEMat',6],['CMat',4]],6,[['300mm',1]],25]
            if usageFactory(pp6) : self.processes.append(pp6)
        if upgrade == '2':
            pp7 = [0,[['HEMat',1],['CMat',2]],4,[['HERockets',1]],25]
            if usageFactory(pp7) : self.processes.append(pp7)
            pp8 = [0,[['HEMat',1],['CMat',2]],4,[['FireRocket',1]],25]
            if usageFactory(pp8) : self.processes.append(pp8)

# POWER PLANTS
class DieselPowerPlant:
    def __init__(self):
        upgrade = input("\nYou are creating a DieselPowerPlant, which upgrade do you wish ? (0:None, 1:PetrolPowerPlant) ")
        self.processes = []
        pp0 = [0,[['LDiesel',25]],5,45,[]]
        if usagePlant(pp0) :self.processes.append(pp0)
        if upgrade=='1':
            pp1 = [0,[['LPetrol',50]],12,90,[]]
            if usagePlant(pp1) : self.processes.append(pp1)

class PowerStation:
    def __init__(self):
        upgrade = input("\nYou are creating a PowerStation, which upgrade do you wish ? (0:None, 1:SulfuricReactor) ")
        self.processes = []
        pp0 = [0,[['LOil',50]],10,90,[]]
        if usagePlant(pp0) :self.processes.append(pp0)
        pp1 = [0,[['Coal',60],['LWater',25]],10,90,[]]
        if usagePlant(pp1) :self.processes.append(pp1)
        elif upgrade=='1':
            pp2 = [0,[['LHOil',50]],10,90,[['Sulfur',1]]]
            if usagePlant(pp2) : self.processes.append(pp2)
            pp3 = [0,[['Coke',60],['LWater',25]],10,90,[['Sulfur',1]]]
            if usagePlant(pp3) : self.processes.append(pp3)

# TOOL FUNCTIONS
def usageFactory(pp):
    print('Do you want to use the process : ',end='')
    printRr(pp[1])
    print(' -> ',end='')
    printRr(pp[3])
    use = input(' ('+str(pp[4])+'s '+str(pp[2])+'MW) ? (y/n) ')
    if use == 'y' : return True

def usagePlant(pp):
    print('Do you want to use the process : ',end='')
    printRr(pp[1])
    print(' -> '+str(pp[2])+'MW',end='')
    if len(pp[4]) > 0 : print(' + ',end='')
    printRr(pp[4])
    use = input(' ('+str(pp[3])+'s)? (y/n) ')
    if use == 'y' : return True

def printRr(list):
    i=0
    for rr in list:
        print(str(rr[1])+rr[0],end='')
        i += 1
        if i != len(list):
            print(' + ',end='')