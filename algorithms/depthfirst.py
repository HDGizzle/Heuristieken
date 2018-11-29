import initialiser as init
import random
import math


# define province dictionary and different senders
provinces = init.province_initialiser("nederland.csv")
sendtypes = ["A", "B", "C", "D", "E", "F", "G"]


visited = [] # blijft intact
stack = ["Groningen"] # wordt gepopt, staat een beginprovince in
print(provinces["Friesland"].sender)
print(provinces[stack[-1]].sender)
print(len(provinces))

while len(visited) != len(provinces):  # zolang er unvisited provinces zijn

    if provinces[stack[-1]].sender == None:       # mocht je geen stap terug hebben genomen wil je deze loop in gaan

        visited.append(stack[-1])           # je gaat een zender toevoegen dus append je hem alvast aan visited

        for neighbor in provinces[stack[-1]].neighbors:

            temp = ["A", "B", "C", "D", "E", "F", "G"]
         # tijdelijk om een lijst met ongebruikte zendtypes over te houden
            for sendtype in sendtypes:

                if provinces[neighbor].sender == sendtype:
                    # print(sendtype)
                    temp.remove(sendtype)
                    print(temp)
                provinces[stack[-1]].sender = temp[0]  # gebruik eerste zender uit de lijst met ongebruikte zendtypes om minimaal aantal verschillende zenders te gebruiken

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

            stack.append(list[0]) # begint bovenaan while loop en dit wordt de nieuwe stack[-1]


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

            stack.append(list[0]) # begint bovenaan while loop en dit wordt de nieuwe stack[-1]

for province in provinces:

    print(provinces[province].sender, province)
