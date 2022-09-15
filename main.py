from xml.etree.ElementTree import tostring
import numpy
import matplotlib.pyplot
from FoxholeData import *

#======== Main Beginning ========

# ==== Asking which type of analysis is wanted ====
# analysistype = input("Which simulation do you want to perform ? ")

# ==== Type 1 Simulation ====

#Buildings
Bld = [
    OilWell(0)
]

Resources = Res.copy()
for key,value in Resources.items():
    value = input('How many '+key+' do you dispose ?')

dt = 1
duration = 110

# ==== SIMULATION ====
# for key,value in Resources.items():
#     print(key+' : '+str(value))
oilWell1 = OilWell(0)

for p in oilWell1.processes:
    p.start()

for t in range(1,duration+1):
    for p in oilWell1.processes:
        if p.update():
            
    print(str(t)+" : "+str(Resources))

for p in oilWell1.processes:
    p.stop()