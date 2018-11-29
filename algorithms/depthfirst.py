import initializer as init
import random
import math


# define province dictionary and different senders
provinces = init.province_initialiser("nederland.csv")
sendtypes = ["A", "B", "C", "D", "E", "F", "G"]



visited = [] # blijft intact
stack = [] # wordt gepopt, staat een beginprovince in

while len(visited) != len(provinces):  # zolang er unvisited provinces zijn

    if stack[-1].sender == None:       # mocht je geen stap terug hebben genomen wil je deze loop in gaan

        visited.append(stack[-1])           # je gaat een zender toevoegen dus append je hem alvast aan visited
        for neighbors in stack[-1]:

            for sendtype in sendtypes:

                temp = sendtypes         # tijdelijk om een lijst met ongebruikte zendtypes over te houden
                for neighbor in neighbors:
                    if neighbor.sender == sendtype:
                        temp.remove(sendtype)

                stack[-1].sender = temp[0]  # gebruik eerste zender uit de lijst met ongebruikte zendtypes om minimaal aantal verschillende zenders te gebruiken

            for neighbor in neighbors:
                if neighbor in visited:
                    pop(stack[-1])          # als alle buren in visited zijn zit je klem en moet je stapje terug, begin weer bovenaan while loop


            # if all neighbors in visited:
            #     pop(stack[-1])          # als alle buren in visited zijn zit je klem en moet je stapje terug, begin weer bovenaan while loop

            else:
                list = []                     # selectie met buren die nog niet visited zijn
                for neighbor in neighbors:
                    if neighbor not in visited:
                        list.append(neighbor)

                stack.append(list[0]) # begint bovenaan while loop en dit wordt de nieuwe stack[-1]


    #
    # else:                           # als je wel een stap terug hebt genomen doe je dit
    #     for neighbors in stack[-1]:
    #
    #         if all neighbors in visited:
    #             pop(stack[-1])          # als alle buren in visited zijn zit je klem en moet je stapje terug, begin weer bovenaan while loop
    #
    #         else:
    #             lijst = []                      # selectie met buren die nog niet visited zijn
    #             for neighbor in neighbors
    #                 if neighbor not in visited:
    #                     lijst.append(neighbor)
    #
    #             stack.append(random lijst provincie)    # begint bovenaan while loop en dit wordt de nieuwe stack[-1]
