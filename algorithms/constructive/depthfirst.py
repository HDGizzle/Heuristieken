<<<<<<< HEAD
import os
import sys
basepath = os.path.abspath(os.path.curdir).split("Heuristieken")[0] + "Heuristieken"
sys.path.append(os.path.join(basepath, "main"))
import checker as check
import random
from collections import defaultdict


def low_variance_picker(possible, usage):
    """
    sorts dictionary of senders based on the frequency of their respective
    usage, which leads to a more even distribution of sender types by given
    preference to the sender with the lowest frequency in placing it
    """
    for sendtype, used in sorted(usage.items(), key=lambda x: x[1]):
        if sendtype in possible:
            return sendtype
    return possible[0]


def depth_first(provinces, senders, combinations):
    """
    depth first is used to try out a given amount of combinations and finds
    outcomes with either the lowest variance or costs
    """

    # places senders in provinces and uses outcome as benchmark
    check.place_senders(provinces, senders)
    benchmark = check.save_outcome(provinces)

    # try n combinations
    for i in range(combinations):

        """
        define a controlled random in order to roam statespace and make search
        replicable
        """
        random.seed(i)

        # define visited as empty set
        visited = set()

        # clear senders from provinces
        check.province_reset(provinces)

        # pick first province to start with
        stack = [list(provinces.keys())[0]]

        # this dictionary keeps track of sender usage
        usage = defaultdict(int)

        # assign sendertype to provinces without neighbors
        for province in provinces:
            if not provinces[province].neighbors:
                provinces[province].sender_placer(provinces, senders)
                usage[provinces[province].sender.type] += 1
                visited.add(province)

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
            for neighbor in provinces[province].neighbors:
                if neighbor not in visited:
                    neighbors.append(neighbor)

            # add all unvisited neighbors to stack and shuffle order
            random.shuffle(neighbors)
            stack.extend(neighbors)

            # define sendtypes
            sender_types = list(senders.keys())

            # remove senders already used with neighbors
            for neighbor in provinces[province].neighbors:
                if provinces[neighbor].sender:
                    if provinces[neighbor].sender.type in sender_types:
                        sender_types.remove(provinces[neighbor].sender.type)

            # assign available sender type based on usage
            sender = low_variance_picker(sender_types, usage)
            provinces[province].sender = senders[sender]
            usage[sender] += 1

        # keep track of outcome
        outcome = check.save_outcome(provinces)

        # check if outcome is more efficient than benchmark
        if check.enhanced_distribution(outcome, benchmark):
            benchmark = outcome
            seed = i

    print(benchmark)
    print(seed)
=======
import os
import sys
basepath = os.path.abspath(os.path.curdir).split("Heuristieken")[0] + "Heuristieken"
sys.path.append(os.path.join(basepath, "initialiser"))
sys.path.append(os.path.join(basepath, "initialiser", "data"))
import initialiser as init
import random
import math
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
for i in range(10000):
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
>>>>>>> 7c45e56609a28d861b4f089a481c3c0a717da091
