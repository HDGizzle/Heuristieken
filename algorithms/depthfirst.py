<<<<<<< HEAD
import os
import sys
basepath = os.path.abspath(os.path.curdir).split("Heuristieken")[0] + "Heuristieken"
sys.path.append(os.path.join(basepath, r"initialiser"))
sys.path.append(os.path.join(basepath, r"initialiser/data"))
from initialiser import province_initialiser as init
=======
import initialiser as init
>>>>>>> ff26648224e89c3a5416c544d567d0895a573371
import random
import math


# define province dictionary and different senders
provinces = init.province_initialiser("usa_borders.csv")
sendtypes = ["A", "B", "C", "D", "E", "F", "G"]

<<<<<<< HEAD
visited = []  # blijft intact
stack = []  # wordt gepopt, staat een beginprovince in

while len(visited) != len(provinces):  # zolang er unvisited provinces zijn

    if stack[-1].sender is None:       # mocht je geen stap terug hebben genomen wil je deze loop in gaan
=======

visited = [] # blijft intact
stack = ["Wyoming"] # wordt gepopt, staat een beginprovince in
# print(len(provinces["Utrecht"].neighbors))
used = []

# print(provinces[stack[-1]].sender)
# print(len(provinces))

for province in provinces:
    if len(provinces[province].neighbors) == 0:
        provinces[province].sender = "A"
        visited.append(province)

while len(visited) != len(provinces):  # zolang er unvisited provinces zijn
    temp = ["A", "B", "C", "D", "E", "F", "G"]

    if provinces[stack[-1]].sender == None:       # mocht je geen stap terug hebben genomen wil je deze loop in gaan
>>>>>>> ff26648224e89c3a5416c544d567d0895a573371

        visited.append(stack[-1])           # je gaat een zender toevoegen dus append je hem alvast aan visited

        for neighbor in provinces[stack[-1]].neighbors:

         # tijdelijk om een lijst met ongebruikte zendtypes over te houden
            if provinces[neighbor].sender in temp:
                # print(sendtype)
                temp.remove(provinces[neighbor].sender)
            provinces[stack[-1]].sender = temp[0]  # gebruik eerste zender uit de lijst met ongebruikte zendtypes om minimaal aantal verschillende zenders te gebruiken
            if temp[0] not in used:
                used.append(temp[0])

        count = 0
        for neighbor in provinces[stack[-1]].neighbors:
            if neighbor in visited:
                count = count + 1

        if count == len(provinces[stack[-1]].neighbors):
            stack.pop()
                         # als alle buren in visited zijn zit je klem en moet je stapje terug, begin weer bovenaan while loop
        else:
            list = []                     # selectie met buren die nog niet visited zijn
            for neighbor in provinces[stack[-1]].neighbors:
                if neighbor not in visited:
                    list.append(neighbor)

<<<<<<< HEAD
<<<<<<< HEAD
            for neighbor in neighbors:
                if neighbor in visited:
                    stack.pop(stack[-1])          # als alle buren in visited zijn zit je klem en moet je stapje terug, begin weer bovenaan while loop
=======
            stack.append(list[0]) # begint bovenaan while loop en dit wordt de nieuwe stack[-1]
>>>>>>> ff26648224e89c3a5416c544d567d0895a573371
=======
            stack.append(random.choice(list)) # begint bovenaan while loop en dit wordt de nieuwe stack[-1]
>>>>>>> 0af3b7378bf7a94ab83339e09144ee6f2aab5e14


    else:                           # als je wel een stap terug hebt genomen doe je dit
        count = 0
        for neighbor in provinces[stack[-1]].neighbors:
            if neighbor in visited:
                count = count + 1

        if count == len(provinces[stack[-1]].neighbors):
            stack.pop()
                         # als alle buren in visited zijn zit je klem en moet je stapje terug, begin weer bovenaan while loop
        else:
            list = []                     # selectie met buren die nog niet visited zijn
            for neighbor in provinces[stack[-1]].neighbors:
                if neighbor not in visited:
                    list.append(neighbor)

            stack.append(random.choice(list)) # begint bovenaan while loop en dit wordt de nieuwe stack[-1]

for province in provinces:

    print(provinces[province].sender, province)
print(used)
