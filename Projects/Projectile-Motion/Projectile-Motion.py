import math
from ExperimentData import ExperimentData

import os
from pathlib import Path

import json

# Gun="RPK-16"
# Guncartridge="5.45x39mm,"
# Gunround="5.45x39mm FMJ"
# v_ms=884
# Building="Burj Khalifa"
# h_m=829.8
# gravity_ms=9.81

def ProjectileFunction(experimentData:ExperimentData):
    time_s= (math.sqrt(2*h_m/gravity_ms))
    DeltaX_m = (math(v_ms*time_s))
    print(f"""In this experiment, I will be using {Gun} from the game "Escape from Tarkov"and use both {Guncartridge} and {Gunround} of my choice to see how far my projectile would go if fired at {Building}""")

# experimentData = {
#    "Gun" : "RPK-16",
#    "Guncartridge" : "5.45x39mm,"
#    "Gunround" : "5.45x39mm FMJ"
#    "v_ms" : 884
#    "Building" : "Burj Khalifa"
#    "h_m" : 829.8
#    "gravity_ms" : 9.81
# }

experimentData0 = ExperimentData("RPK-16", "5.45x39mm", "5.45x39mm FMJ", 884, "Burj Khalifa", 829.8, 9.81)
experimentData1 = ExperimentData("")
ProjectileFunction(experimentData)

myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath , 'ExperimentData.json')

with open(myOutputFilePath, 'w') as outfile: 
    json.dump(experimentData.__dict__ , outfile)
    