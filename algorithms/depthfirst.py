import os
import sys
basepath = os.path.abspath(os.path.curdir).split("Heuristieken")[0] + "Heuristieken"
sys.path.append(os.path.join(basepath, "initialiser"))
sys.path.append(os.path.join(basepath, "initialiser", "data"))
import initialiser
import random
import math
<<<<<<< HEAD
import sys
from collections import Counter, defaultdict

def pick_sendtype(possible, usage):
    # even iets meer uitleg:
    # sorted(usage.items(), key=lambda x: x[1]) --> sorteert het aantal keer voorkomen van de zendertypes van laag naar hoog
    # met je gesorteerde frequenties ga je kijken naar of 1 meeredere van deze in het lijstje van ongebruikte zendtypes zit
    for sendtype, used in sorted(usage.items(), key=lambda x: x[1]):
        # als de eerste (minst gebruikte dus) uit usage in possible zit, gebruik je die, anders de 2e, anders de 3e etc.
        if sendtype in possible:
            return sendtype

    # als geen van de gebruikte er in zit, dus usage niet voorkomt in possible, dan gebruik je de eerste de beste uit het lijstje (een nieuwe zender dus)
    return possible[0]

# this list will later contain random seeds for output of 4 sendtypes
right_seeds = []

# try 10.000 combinations
for i in range(20):
    # define a controlled random in order to roam state-space and make search replicable
    random.seed(i)

    # call data
    provinces = init.province_initialiser("nederland.csv")

    # define visited as empty set --> a set is faster to search through than a list
    visited = set()

    # define stack and starting province
    stack = [provinces["Utrecht"]]

    # define the existence of a dict which will be used later keep track of how frequent each sendtype is used
    usage = defaultdict(int)

    # assign sendertype to provinces without neighbors
    for province in provinces:
        if not provinces[province].neighbors:
            provinces[province].sender = "A"
            visited.add(province)
            usage["A"] += 1

    # as long as stack contains provinces
    while stack:
        province = stack.pop()

        # start on top of loop if province has already been visited
        if province in visited:
            continue

        # append current province to visited
        visited.add(province)

        # define unvisited neighbors list
        neighbors = []
        for neighbor in province.neighbors:
            if neighbor not in visited:
                neighbors.append(provinces[neighbor])

        # add all unvisited neighbors to stack and shuffle order
        random.shuffle(neighbors)
        stack.extend(neighbors)

        # define sendtypes
        sender_types = ["A", "B", "C", "D", "E", "F", "G"]

        # remove all sender types present in neighbors
        for neighbor in province.neighbors:
            if provinces[neighbor].sender in sender_types:
                sender_types.remove(provinces[neighbor].sender)

        # assign least used possible sendtype to province
        sender = pick_sendtype(sender_types, usage)
        province.sender = sender
        usage[sender] += 1


    # if only 4 senders are used:
    if len(usage) == 4:
        # print all provinces and sendtypes
        for province in provinces:
            print(provinces[province].sender, province)
        # print frequencies of each sendtype
        print(usage)
        # print according seed
        print(i)
        # append to list of seeds returning 4 sendtypes
        right_seeds.append(i)

    # commands to stop the programme after a number x of solutions with 4 sendtypes are found and prints the according seeds
    if len(right_seeds) == 20:
        # this is a list of the seeds returning 4 sendtypes
        print(right_seeds)
        break
=======


# define province dictionary and different senders
provinces = initialiser.province_initialiser("usa_borders.csv")
sendtypes = ["A", "B", "C", "D", "E", "F", "G"]

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

            stack.append(random.choice(list)) # begint bovenaan while loop en dit wordt de nieuwe stack[-1]


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
>>>>>>> 586a6c974355adcb4a764e1657e79c1c4504213e
