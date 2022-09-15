Res = { 
    'Oil': 0,
    'Water': 0,
    'Petrol': 0,
    'HeavyOil': 0,
    'EnrichedOil': 0,
    'Coal': 0,
    'Coke': 0,
    'Sulfur': 0,
    'Concrete': 0,
    'Salvage': 0,
    'CMat': 0,
    'BMat': 0,
    'AMat1': 0,
    'AMat2': 0,
    'ElecPower': 0,
}

class Process:
    def __init__(self,inputs,outputs,duration,auto):
        self.inputs = inputs
        self.outputs = outputs
        self.state = False
        self.timer = 0
        self.duration = duration
        self.autoRestart = auto
    
    def start(self):
        self.state = True
    
    def stop(self):
        self.state = False
    
    def update(self):
        if self.state == True:
            if self.timer == self.duration :
                self.timer = 0
                self.state = False
                return True
            else :
                self.timer += 1
                return False
        return False


class OilWell:
    def __init__(self,upgrade):
        self.tier = upgrade
        self.processes = [Process([],["Oil",1],50,)]

