from factions import faction
import random


facs = []

for i in range(10):
    facs.append(faction.Faction(
        name=f"Faction {i}",
        force=random.randint(0,5),
        wealth=random.randint(0,5),
        cunning=random.randint(0,5),
    ))

for fac in facs:
    print(fac)
