import numpy as np

raw_data = [
# Stationnary Harvester (Scrap)          Time   Elec     LDi  Oil  LOil  Wat  LWat  Pet  LPet  HOil  LHOil  EOil  LEOil  Coal  Sulfur  Compo  Coke  CMat  Salv  PCMat  SCMat  AMat1  AMat2  AMat3  AMat4  AMat5  Pipe  Conc  Sand  Wire  MetBar  EMat  HEMat  Flame  75  94.5  120  150  250  300  HER  FireR  
                                        [12   ,[0       ,0   ,0   ,0    ,0   ,0    ,0   ,-4   ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,0    ,50   ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Salvage Harvest'],
# Water Pump
                                        [50   ,[0       ,0   ,0   ,0    ,1   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Water Basic'],
# Electric Water Pump
                                        [40   ,[0       ,0   ,0   ,0    ,1   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Water Advanced (no pipe)'],
                                        [50   ,[-0.5    ,0   ,0   ,0    ,0   ,60   ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Water Advanced (pipe)'],
# Oil Well
                                        [50   ,[0       ,0   ,1   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Oil basic'],
# Electric oil Well
                                        [26   ,[-2      ,0   ,1   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Oil Advanced (no pipe)'],
                                        [40   ,[-2      ,0   ,0   ,75   ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Oil Advanced (pipe)'],
# Fracker
                                        [40   ,[-3      ,0   ,2   ,0    ,0   ,-25  ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Water -> Oil (no pipe)'],
                                        [30   ,[-3      ,0   ,0   ,75   ,0   ,-25  ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Water -> Oil (Oil)'],
# Stationnary Harvester (Coal)
                                        [12   ,[0       ,0   ,0   ,0    ,0   ,0    ,0   ,-4   ,0    ,0     ,0    ,0     ,50   ,0      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Coal Harvest'],
# Stationnary Harvester (Sulfur)
                                        [12   ,[0       ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,-4    ,0    ,0     ,0    ,6      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Sulfur Harvest'],
# Stationnary Harvester (Component)
                                        [12   ,[0       ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,-4    ,0    ,0     ,0    ,0      ,6     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Component Harvest'],
#=========================================================================================================================================================================================================================================================================================================
# Materials Factory                      Time   Elec     LDi  Oil  LOil  Wat  LWat  Pet  LPet  HOil  LHOil  EOil  LEOil  Coal  Sulfur  Compo  Coke  CMat  Salv  PCMat  SCMat  AMat1  AMat2  AMat3  AMat4  AMat5  Pipe  Conc  Sand  Wire  MetBar  EMat  HEMat  Flame  75  94.5  120  150  250  300  HER  FireR
                                        [25   ,[-2      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,1    ,-20  ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Salvage->CMat'],
# Forge
                                        [60   ,[-2      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,-180 ,0    ,-20  ,0     ,0     ,1     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Salvage + Coke -> AMat1'],
                                        [60   ,[-2      ,0   ,0   ,0    ,0   ,0    ,0   ,-150 ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,0    ,-20  ,0     ,0     ,0     ,1     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Salvage + Petrol -> AMat2'],
# Metal Press
                                        [25   ,[-4      ,0   ,0   ,0    ,0   ,0    ,0   ,-25  ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,3    ,-20  ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Salvage + Petrol -> CMat'],
# Smelter
                                        [25   ,[-4      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,-25  ,3    ,-20  ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Salvage + Coke -> CMat'],
# Recycler
                                        [25   ,[-2      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,1    ,-25  ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,5    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Salvage -> CMat + Sandbag'],
                                        [25   ,[-2      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,1    ,-25  ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,5    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Salvage -> CMat + BarbedWire'],
#=========================================================================================================================================================================================================================================================================================================
#  Metalworks Factory                    Time   Elec     LDi  Oil  LOil  Wat  LWat  Pet  LPet  HOil  LHOil  EOil  LEOil  Coal  Sulfur  Compo  Coke  CMat  Salv  PCMat  SCMat  AMat1  AMat2  AMat3  AMat4  AMat5  Pipe  Conc  Sand  Wire  MetBar  EMat  HEMat  Flame  75  94.5  120  150  250  300  HER  FireR
                                        [60   ,[-5      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,-20   ,0    ,-3   ,0    ,1     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'CMat + Component -> PCMat'],
                                        [120  ,[-5      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,0    ,0    ,-3    ,0     ,0     ,0     ,0     ,0     ,0     ,1    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'PCMat -> Pipe'],
# Blast Furnace
                                        [60   ,[-8      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,-6    ,0    ,0     ,0    ,0      ,-55   ,0    ,-3   ,0    ,3     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'CMat + Component + Heavy oil -> PCMat3'],
                                        [120  ,[-5      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,-20    ,0     ,0    ,-3   ,0    ,0     ,0     ,0     ,0     ,1     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'PCMat + Heavy Oil -> AMat3'],
                                        [120  ,[-5      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,-66   ,0    ,0     ,0    ,0      ,0     ,0    ,0    ,0    ,-1    ,0     ,0     ,0     ,0     ,1     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'CMat + Sulfur -> AMat4'],
# Recycler
                                        [60   ,[-5      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,-20   ,0    ,-3   ,0    ,1     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,1      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'CMat + Component -> PCMat + Metal Bar'],
                                        [90   ,[-4      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,1     ,0    ,0    ,-200 ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Salvage -> Component'],
# Engineering Station
                                        [160  ,[-9      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,-6    ,0    ,0     ,0    ,0      ,-20   ,0    ,0    ,0    ,-3    ,1     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'PCMat + Component + Heavy Oil -> SCMat'],
                                        [160  ,[-8      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,-3    ,0    ,-20    ,-20   ,0    ,0    ,0    ,-3    ,3     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'PCMat + Component + Sulfur + Enriched Oil -> SCMat'],
                                        [160  ,[-8      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,-6    ,0    ,0      ,0     ,0    ,0    ,0    ,0     ,-1    ,0     ,0     ,0     ,0     ,1     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'SCMat + Enriched Oil -> AMat5'],
#=========================================================================================================================================================================================================================================================================================================
# Coal Refinery                          Time   Elec     LDi  Oil  LOil  Wat  LWat  Pet  LPet  HOil  LHOil  EOil  LEOil  Coal  Sulfur  Compo  Coke  CMat  Salv  PCMat  SCMat  AMat1  AMat2  AMat3  AMat4  AMat5  Pipe  Conc  Sand  Wire  MetBar  EMat  HEMat  Flame  75  94.5  120  150  250  300  HER  FireR
                                        [120  ,[-3      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,-200 ,0      ,0     ,180  ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Coal -> Coke'],
# Coke Furnace
                                        [120  ,[-3      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,-200 ,15     ,0     ,165  ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Coal -> Coke + Sulfur'],
# Coal Liquifier
                                        [120  ,[-4      ,0   ,0   ,50   ,0   ,-75  ,0   ,0    ,0    ,0     ,0    ,0     ,-300 ,0      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,1    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Coal + Water'],
# Advanced Coal Liquifier
                                        [180  ,[-4      ,0   ,0   ,0    ,0   ,-150 ,0   ,0    ,0    ,60    ,0    ,0     ,-300 ,0      ,0     ,260  ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Coal + Water -> Coke + Heavy Oil'],
#=========================================================================================================================================================================================================================================================================================================
# Oil Refinery                           Time   Elec     LDi  Oil  LOil  Wat  LWat  Pet  LPet  HOil  LHOil  EOil  LEOil  Coal  Sulfur  Compo  Coke  CMat  Salv  PCMat  SCMat  AMat1  AMat2  AMat3  AMat4  AMat5  Pipe  Conc  Sand  Wire  MetBar  EMat  HEMat  Flame  75  94.5  120  150  250  300  HER  FireR
                                        [150  ,[-1      ,0   ,0   ,-150 ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Oil -> Petrol'],
# Reformer
                                        [150  ,[-1      ,0   ,0   ,-120 ,0   ,-30  ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Oil + Water -> Petrol'],
# Cracking Unit
                                        [160  ,[-1.5    ,0   ,0   ,-150 ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Heavy Oil'],
# Petrochimical Plant
                                        [160  ,[-2      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,-90   ,0    ,0     ,0    ,-20    ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Enriched Oil'],
#=========================================================================================================================================================================================================================================================================================================
# Ammunition Factory                     Time   Elec     LDi  Oil  LOil  Wat  LWat  Pet  LPet  HOil  LHOil  EOil  LEOil  Coal  Sulfur  Compo  Coke  CMat  Salv  PCMat  SCMat  AMat1  AMat2  AMat3  AMat4  AMat5  Pipe  Conc  Sand  Wire  MetBar  EMat  HEMat  Flame  75  94.5  120  150  250  300  HER  FireR
                                        [25   ,[-4      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,-1   ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,-1    ,1     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Flame Ammo'],
                                        [30   ,[-4      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,-5   ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,-6    ,0     ,0  ,0    ,0   ,0   ,1   ,0   ,0   ,0   ],'250mm'],
# Large Shell Factory
                                        [25   ,[-4      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,-2   ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,-2    ,0     ,1  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'75mm'],
                                        [25   ,[-4      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,-2   ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,-2    ,0     ,0  ,1    ,0   ,0   ,0   ,0   ,0   ,0   ],'94.5mm'],
                                        [15   ,[-4      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,-2   ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,-3   ,0     ,0     ,0  ,0    ,1   ,0   ,0   ,0   ,0   ,0   ],'120mm'],
                                        [20   ,[-4      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,-3   ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,-2    ,0     ,0  ,0    ,0   ,1   ,0   ,0   ,0   ,0   ],'150mm'],
                                        [25   ,[-6      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,-4   ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,-6    ,0     ,0  ,0    ,0   ,0   ,0   ,1   ,0   ,0   ],'300mm'],
# Rocket Factory
                                        [25   ,[-4      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,-2   ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,-1    ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,1   ,0   ],'HE Rockets'],
                                        [25   ,[-4      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,-2   ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,-1    ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,1   ],'Fire Rockets'],
#=========================================================================================================================================================================================================================================================================================================
# Diesel Power Plant                     Time   Elec     LDi  Oil  LOil  Wat  LWat  Pet  LPet  HOil  LHOil  EOil  LEOil  Coal  Sulfur  Compo  Coke  CMat  Salv  PCMat  SCMat  AMat1  AMat2  AMat3  AMat4  AMat5  Pipe  Conc  Sand  Wire  MetBar  EMat  HEMat  Flame  75  94.5  120  150  250  300  HER  FireR
                                        [45   ,[5       ,-25 ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Diesel -> Electricity'],
# Petrol Power Plant
                                        [90   ,[12      ,0   ,0   ,0    ,0   ,0    ,-50 ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Petrol -> Electricity'],
# Power Station
                                        [90   ,[10      ,0   ,0   ,-50  ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,0      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Oil -> Electricity'],
                                        [90   ,[10      ,0   ,0   ,0    ,0   ,-25  ,0   ,0    ,0    ,0     ,0    ,0     ,-60  ,0      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Coal -> Electricity'],
# Sulfuric Reactor
                                        [120  ,[16      ,0   ,0   ,0    ,0   ,0    ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,1      ,0     ,0    ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Heavy Oil -> Electricity + Sulfur'],
                                        [120  ,[16      ,0   ,0   ,0    ,0   ,-25  ,0   ,0    ,0    ,0     ,0    ,0     ,0    ,1      ,0     ,-60  ,0    ,0    ,0     ,0     ,0     ,0     ,0     ,0     ,0     ,0    ,0    ,0    ,0    ,0      ,0    ,0     ,0     ,0  ,0    ,0   ,0   ,0   ,0   ,0   ,0   ],'Coke -> Electricity + Sulfur'],
]

ResNames = ['Elec','LDi','Oil','LOil','Wat','LWat','Pet','LPet','HOil','LHOil','EOil','LEOil','Coal','Sulfur','Compo','Coke','CMat','Salv','PCMat','SCMat','AMat1','AMat2','AMat3','AMat4','AMat5','Pipe','Conc','Sand','Wire','MetBar','EMat','HEMat','Flame','75mm','94.5mm','120mm','150mm','250mm','300mm','HERkt','FireRkt']
Buildings = [
    ['Stationnary Harvester (Scrap)',[0],       [                                                                                                                                   ]],
    ['Water Pump',[1],                          [['Electric Water Pump',[2,3]],                                                                                                     ]],
    ['Oil Well',[4],                            [['Electric Oil Well',[5,6]],               ['Fracker',[7,8]],                                                                      ]],
    ['Stationnary Harvester (Coal)',[9],        [                                                                                                                                   ]],
    ['Stationnary Harvester (Sulfur)',[10],     [                                                                                                                                   ]],
    ['Stationnary Harvester (Component)',[11],  [                                                                                                                                   ]],
    ['Materials Factory',[12],                  [['Forge',[13,14]],                         ['Metal Press',[15]],       ['Smelter',[16]],                     ['Recycler',[17,18]], ]],
    ['Metalworks Factory',[19,20],              [['Blast Furnace',[21,22,23]],              ['Recycler',[24,25]],       ['Engineering Station',[26,27,28]],                         ]],
    ['Coal Refinery',[29],                      [['Coke Furnace',[30]],                     ['Coal Liquifier',[31]],    ['Advanced Coal Liquifier',[32]],                           ]],
    ['Oil Refinery',[33],                       [['Reformer',[34]],                         ['Cracking Unit',[35]],     ['Petrochimical Plant',[36]],                               ]],
    ['Ammunition Factory',[37,38],              [['Large Shell Factory',[39,40,41,42,43]],  ['Rocket Factory',[44,45]],                                                             ]],
    ['Diesel Power Plant',[46],                 [['Petrol power Plant',[47]],                                                                                                       ]],
    ['Power Station',[48,49],                   [['Sulfuric Reactor',[50,51]],                                                                                                      ]],
]

# ===== FONCTIONS SECONDAIRES =====
def printData(data):
    for ligne in data:
        for rr in ligne:
            print("{:.1f},  ".format(rr),end='')
        print('')

def printLine(data):
    i = 0
    for dd in data:
        if (i+13)//13 == 0 : print('\n')
        print(ResNames[i]+" : {:.2f},\t".format(dd),end=' ')
        i = i+1

def computeOutput(input,data):
    return np.dot(input,data)

# ====================== MAIN ======================

# ===== INIT =====
p = len(raw_data)
r = len(raw_data[0][1])
data = np.zeros([p,r])
for pp in range(p):
    for rr in range(r):
        if rr != 0 :
            data[pp][rr] = raw_data[pp][1][rr]/raw_data[pp][0]
        else :
            data[pp][rr] = raw_data[pp][1][rr]

ListBuildings = [[], [], [], [], [], [], [], [], [], [], [], [], []]
inputs = np.zeros(p)
outputs = np.zeros(r)

# ===== INPUT =====
action = 'x'
while action != 'c':
    action = input('\nDo you want to add a building or start the calulation ? (b/c) ')
    if action == 'b':
        print("\nBuildings are : 0:Stationnary Harvester (Scrap), 1:Water Pump, 2:Oil Well, 3:Stationnary Harvester (Coal), 4:Stationnary Harvester (Sulfur), 5:Stationnary Harvester (Component), 6:Materials Factory, 7:Metalworks Factory, 8:Coal Refinery, 9:Oil Refinery, 10:Ammunition Factory, 11:Diesel Power Plant, 12:Power Station")
        bb = int(input('Select a building : '))
        if bb in range(0,13):
            availableProcesses = []
            for pp in Buildings[bb][1]: 
                availableProcesses.append(pp)
            if len(Buildings[bb][2]) != 0:
                print("Upgrades available are : 0:None, ",end='')
                for kk in range(len(Buildings[bb][2])):
                    print(str(kk+1)+':'+Buildings[bb][2][kk][0]+' ',end='')
                upgrade = int(input('\nSelect an upgrade : '))
                if upgrade != 0:
                    for pp in Buildings[bb][2][upgrade-1][1] : availableProcesses.append(pp)
        processUsed = []
        for pp in availableProcesses:
            use = input('Do you want to use the process '+str(raw_data[pp][2])+' ? (y,n) ')
            if use=='y': processUsed.append(pp)
        for pp in processUsed : inputs[pp] += 1


# ===== CALCULATION =====
outputs=computeOutput(inputs,data)

# ===== OUTPUT =====
printLine(outputs)