import sys
from json import load, dump
from pprint import pprint
index = sys.argv[1]
with open("rawdata.json", "r") as infile:
    data = load(infile)
current = data[index]
newBOI = {
                            "metacarpal":{
                                "direction" : tuple(finger.bone(0).direction),
                                "length" : finger.bone(0).length
                            },
                            "proximal":{
                                "direction" : tuple(finger.bone(1).direction),
                                "length" : finger.bone(1).length
                            },
                            "intermediate":{
                                "direction" : tuple(finger.bone(2).direction),
                                "length" : finger.bone(2).length
                            },
                            "distal":{
                                "direction" : tuple(finger.bone(3).direction),
                                "length" : finger.bone(3).length
                            }
                            }
pprint(newBOI)
current.append(newBOI)
data[index] = current
with open("rawdata.json","w") as outfile:
    dump(data, outfile)
