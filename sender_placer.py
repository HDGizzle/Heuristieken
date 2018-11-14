"""
this script places senders in different provinces under the constraint that
bordering provinces cannot have the same sender type
"""

# imports libraries
import pandas
from province_class import Province
from sender_class import Sender

# define global variables
SENDERS = {}
PROVINCES = {}
INPUT_CSV = "russia_borders.csv"


def sender_initialiser():
    """
    initializes seven sendertypes and adds them to global dictionary
    """

    # sender types range from A-G
    sender_types = [1, 2, 3, 4, 5, 6, 7, 8]

    # for first project sender costs are initialised to zero
    costs = 0

    # adds all different sender type objects to SENDERS
    for char in sender_types:
        SENDERS[char] = Sender(char, costs)


def province_initialiser():
    """
    initializes all province objects and adds them global dictionary
    provinces are imported from csv files
    """

    # opens csv file containing province data
    with open(INPUT_CSV) as myfile:
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
            PROVINCES[name] = Province(name, neighbors)


def neighbor_sorted_provinces():
    """
    this function uses the Welsh Powell algoritm to find a solution for the
    placing of senders in provinces under color graphing constraints
    http://mrsleblancsmath.pbworks.com/w/file/fetch/46119304/vertex%20coloring%20algorithm.pdf
    """

    # puts provinces in pools based on number of connections
    connections_sort = {}

    # iterates over province objects
    for province in PROVINCES:

        # takes number of neighbors for province
        no_neighbors = len(PROVINCES[province].neighbors)

        # puts province name in sorted list based on no_neighbors
        if no_neighbors in connections_sort:

            # adds name of province to dict pool based on no_connections
            connections_sort[no_neighbors].append(PROVINCES[province].name)

        # updates no_connections and connections_sort dictionary
        else:

            # new list for pool of provinces sharing no_neighbors is added
            connections_sort[no_neighbors] = [PROVINCES[province].name]

    # returns sorted pools dictionary
    return connections_sort


def welsh_powell(province_pools):
    """
    this function uses the Welsh Powell algoritm to find a solution for the
    placing of senders in provinces under color graphing constraints
    http://mrsleblancsmath.pbworks.com/w/file/fetch/46119304/vertex%20coloring%20algorithm.pdf
    """

    # lists all numbers of connections from high to low
    connections = sorted(province_pools, reverse=True)

    # iterates over senders
    for sender in SENDERS:
        # iterates over province pools
        for connection in connections:

            # iterates over provinces in province pools
            province_pool = province_pools[connection]
            for province_name in province_pool:

                # extracts province object
                province = PROVINCES[province_name]

                # check for presence of sender in neighbor
                present = 0

                # iterate over neighbors
                for neighbor in province.neighbors:

                    # check if sender neighbor corresponds to current sender
                    if PROVINCES[neighbor].sender == sender:
                        present = 1

                # place sender if sender is not in neighbors
                if present == 0:

                    # place sender
                    province.sender = sender

                    # remove province from pool
                    province_pools[connection].remove(province_name)

                    print(sender)

                    # check if pool still contains provinces
                    if len(province_pools[connection]) == 0:

                        # if not skip pool
                        connections.remove(connection)


if __name__ == "__main__":
    """
    loads provinces and senders and finds optimal solution using algoritm
    """

    # initializes all senders and adds them to SENDERS
    sender_initialiser()

    # initializes all province objects and adds them to PROVINCES
    province_initialiser()

    # returns pools of provinces based on number of neighbors into dictionary
    sorted_provs = neighbor_sorted_provinces()

    welsh_powell(sorted_provs)

    # works out sender solutions
    # welsh_powell()
    for province in PROVINCES:
        if not (PROVINCES[province].sender):
            print('NEEN')
            print(PROVINCES[province].name)
        for neighbor in PROVINCES[province].neighbors:
            if PROVINCES[neighbor].sender == PROVINCES[province].sender:
                print('WERKT NIET')
                print(f'{PROVINCES[neighbor].name}, {PROVINCES[province].name},\
                {PROVINCES[province].sender}')

        # print(PROVINCES[province].name)
    #     print(PROVINCES[province].sender)
    #     # print(f'//PROVINCES[province]//')
