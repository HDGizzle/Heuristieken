"""
initializes province and dictionary objects and returns them as a dictionary
also uses a function to sort provinces in pools based on shared amount of
connections
"""

# import libraries and files
import os
import sys
basepath = os.path.abspath(os.path.curdir).split("Heuristieken")[0] + "Heuristieken"
sys.path.append(os.path.join(basepath, "main", "objects"))
sys.path.append(os.path.join(os.path.abspath(os.path.curdir), "data"))
import pandas
from province_class import Province
from sender_class import Sender


def province_initialiser(INPUT_CSV):
    """
    initializes all province objects and adds them global dictionary
    provinces are imported from csv files
    """

    # dictionary containing all province objects with name as key
    provinces = {}

    # opens csv file containing province data
    with open(os.path.join(basepath, "initialiser", "data", INPUT_CSV)) as myfile:

        # checks which csv is imported
        if 'nederland.csv' in INPUT_CSV:
            datafile = pandas.read_csv(myfile, delimiter=';')
        else:
            datafile = pandas.read_csv(myfile)

        # iterates over rows in csv file
        for i in range(len(datafile)):

            # extracts province name and neighbors as a list
            name = datafile["name"][i].strip()
            neighbors = str(datafile["neighbors"][i]).split(", ")

            # replaces pandas designation 'nan' for empty with empty list
            if neighbors[0] in "nan":
                neighbors = []

            # adds new province object to PROVINCES
            provinces[name] = Province(name, neighbors)

    # returns dictionary containing province objects
    return provinces


def sender_initialiser():
    """
    initializes seven sendertypes and adds them to dictionary
    """
    # dictionary containing all sender object with type as key
    senders = {}

    # sender types range from A-G
    sender_types = [1, 2, 3, 4, 5, 6, 7]
    sender_costs = [12,	26,	27,	30,	37,	39,	41]

    # adds all different sender type objects to SENDERS
    for i in range(len(sender_types)):
        senders[sender_types[i]] = Sender(sender_types[i], sender_costs[i])

    # return dictionary containing sender objects
    return senders


def neighbor_sorted_provinces(provinces):
    """
    puts provinces in sorted lists based on the shared amount of connections
    """

    # puts provinces in pools based on number of connections
    connections_sort = {}

    # iterates over province objects
    for province in provinces:

        # takes number of neighbors for province
        no_neighbors = len(provinces[province].neighbors)

        # puts province name in sorted list based on no_neighbors
        if no_neighbors in connections_sort:

            # adds name of province to dict pool based on no_connections
            connections_sort[no_neighbors].append(provinces[province].name)

        # updates no_connections and connections_sort dictionary
        else:

            # new list for pool of provinces sharing no_neighbors is added
            connections_sort[no_neighbors] = [provinces[province].name]

    # returns sorted pools dictionary
    return connections_sort


def total_costs(provinces):
    """
    this function returns the total amount of costs given the senders placed
    """
    costs = 0
    for province in provinces:
        costs += provinces[province].sender.costs
    print(costs)
