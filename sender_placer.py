"""
this script places senders in different provinces under the constraint that
bordering provinces cannot have the same sender type
"""

# imports libraries
import pandas
import copy
from province_class import Province
from sender_class import Sender

# define global variables
SENDERS = {}
PROVINCES = {}
INPUT_CSV = 'nederland.csv'


def sender_initialiser():
    """
    initializes seven sendertypes and adds them to global dictionary
    """

    # sender types range from A-G
    sender_types = [1, 2, 3, 4, 5, 6, 7]

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
        datafile = pandas.read_csv(myfile, delimiter=';') # delimiter=';'

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

    provinces_test = copy.deepcopy(PROVINCES)

    # lists all numbers of connections from high to low
    connections = sorted(province_pools, reverse=True)

    senders_needed = 0

    # iterates over senders
    for sender in SENDERS:

        # iterates over province pools
        for connection in connections:

            # iterates over provinces in province pools
            province_pool = province_pools[connection]
            for province_name in province_pool:

                # extracts province object
                province = provinces_test[province_name]

                # check for presence of sender in neighbor
                present = False

                # iterate over neighbors
                for neighbor in province.neighbors:

                    # check if sender neighbor corresponds to current sender
                    if provinces_test[neighbor].sender == sender:
                        present = True

                # place sender if sender is not in neighbors
                if not present and not province.sender:

                    # place sender
                    province.sender = sender
                    senders_needed = sender

    if senders_needed < 4:
        print(senders_needed)


def clusters():
    """
    calculates the minimum amount of senders need to fill the map based on an
    assessment of the interconnectedness of all neighbors, i.e. clusters
    """

    # dictionary to keep track of all cluster pools based on length
    clusters = {}

    max_interconnections = 0

    # iterate over province objects
    for province in PROVINCES:

        # iterate over all neighbors of given province
        for neighbor in PROVINCES[province].neighbors:
            cluster_participants = [PROVINCES[province].name, neighbor]

            # connections is by default 1 for a neighbor
            interconnections = 1

            # iterate over neighbors of the selected neighbor
            for other_neighbor in PROVINCES[province].neighbors:

                # check if neighbor is in neighbor of in neighbors
                if other_neighbor in PROVINCES[neighbor].neighbors:

                    # add neighbor to given cluster
                    cluster_participants.append(other_neighbor)
                    interconnections += 1

            if interconnections in clusters:
                clusters[interconnections].append(cluster_participants)

            else:
                clusters[interconnections] = cluster_participants

            # keep track of max interconnections measured
            if interconnections > max_interconnections:
                max_interconnections = interconnections

    # return the dictionary containing all clusters per province
    for pool in clusters:
        for i in range(len(clusters[pool])):
            if isinstance(clusters[pool][i], str):
                clusters[pool][i] = [clusters[pool][i]]

    return(clusters, max_interconnections)


def sender_placer(name, provinces_test, senders_available):
    """
    places senders in a province
    """
    # check what senders are usable
    for sender in senders_available:
        usable = True

        # checks senders type for other neighbors
        for neighbor in provinces_test[name].neighbors:

            # if sender is with neighbor, sender cannot be used
            if sender == provinces_test[neighbor].sender:
                usable = False

        # places sender if usable
        if usable:
            provinces_test[name].sender = sender

def greedy_cluster(clusters, current_cluster, provinces_test, senders_available):

    # iterate over names in cluster
    for province in current_cluster:

        # check if sender is already placed
        if not provinces_test[province].sender:
            sender_placer(provinces_test[province].name, provinces_test, senders_available)

    for pool in clusters:
        for i in range(len(clusters[pool])):
            if current_cluster == clusters[pool][i]:
                clusters[pool][i] == []

    # iterate over names in cluster
    for province in current_cluster:
        for neighbor in provinces_test[province].neighbors:
            if not provinces_test[neighbor].sender and neighbor not in current_cluster:
                for pool in clusters:
                    for cluster in clusters[pool]:
                        if neighbor in cluster and cluster != current_cluster:
                            greedy_cluster(clusters, cluster, provinces_test, senders_available)


    # iterate over all provinces and clusters it participates in

# def recursive_placer(province_name, provinces_test, visited_provinces, senders_available):

    # # add provinces to visited provinces
    # visited_provinces.append(province_name)
    #
    # sender_placer(province_name, provinces_test, senders_available)
    #
    # # repeat recursion for unvisited provinces
    # for neighbor in provinces_test[province_name].neighbors:
    #     if neighbor not in visited_provinces:
    #         sender_placer(neighbor, provinces_test, visited_provinces)

if __name__ == "__main__":
    """
    loads provinces and senders and finds optimal solution using algoritm
    """

    # initializes all senders and adds them to SENDERS
    sender_initialiser()

    # initializes all province objects and adds them to PROVINCES
    province_initialiser()

    # returns pools of provinces based on number of neighbors into dictionary
    province_pools = neighbor_sorted_provinces()

    # create a dictionary to keep track of all different sortings of each pool
    pool_sorts = {}

    # sorts every pool by changing each position by 1 over length of list
    for pool in province_pools:

        # add sortings of each pool to list
        pool_sorts[pool] = []

        # number of variations equals length of list
        len_list = len(province_pools[pool])

        # create for every variation a list to be filled in differently ordered
        for i in range(len_list):

            # generates empty list
            order = [None] * len_list

            # fills in the list using different orders
            for j in range(len_list):

                # position of each name is moved by one every iteration of i
                order[j] = province_pools[pool][(j + i) % (len_list)]

            print(order)
            # add newly ordered pool to dictionary
            pool_sorts[pool].append(order)

    # keeps track of the number of countries in every individual pool
    list_counter = []
    list_cursor = [0] * len(province_pools)

    # iterate over pool and save length of pool to list_counter
    for pool in province_pools:
        list_counter.append(len(province_pools[pool]) - 1)

    # keeps track of all variations
    variation = 0

    # makes all possible combines of available sorts in pools
    while list_counter[-1] >= list_cursor[-1]:

        # generate a new dictionary for each iteration
        dictionary = {}

        for counter, pool in enumerate(province_pools):
            dictionary[pool] = pool_sorts[pool][list_cursor[counter]]

        # try a new variation
        list_cursor[variation] += 1

        # iterates over amount of pools
        for i in range(1, len(province_pools)):

            """
            if the cursor has finished all variations for a given pool, the
            cursor for the past pool is reset to zero and starts cursing in
            the new pool
            """
            if list_counter[i - 1] < list_cursor[i - 1]:
                list_cursor[i] += 1
                list_cursor[i - 1] = 0

        # execute wellsh powel for the given variation
        # welsh_powell(dictionary)
    #
    list = clusters()
    clusters = list[0]
    max_interconnections = list[1]


    # use a copy of all provinces
    provinces_test = copy.deepcopy(PROVINCES)
    #
    # keeps track of provinces visited through algoritm
    visited_provinces = []

    # senders to use is based on minimum amount needed
    senders_available = []

    for i in range(1, (max_interconnections + 1)):
        senders_available.append(i)

    for pool in clusters:
        for cluster in clusters[pool]:
            greedy_cluster(clusters, cluster, provinces_test, senders_available)

    # # fills all provinces without neighbors
    # for province in provinces_test:
    #
    #     # checks if provinces has no neighbors
    #     if not provinces_test[province].neighbors:
    #
    #         # places sender
    #         provinces_test[province].sender = senders_available[0]
    #
    #         # adds provinces to visited provinces
    #         visited_provinces.append(province)
    #
    # # fills a map based on the minimum amount of senders needed
    # for province in provinces_test:
    #     sender_placer(province, provinces_test, senders_available)
    # #
    for province in provinces_test:
        # print(province)
        if not provinces_test[province].sender:
            print(f'{province} geen zender')
        for neighbor in provinces_test[province].neighbors:
            if provinces_test[province].sender == provinces_test[neighbor].sender:
                if provinces_test[province].sender:
                    print('overlap')
