"""
this file returns the amount of clusters in a given map and calculates the
bounds of the state space based here on
"""

def clusters(provinces):
    """
    finds all clusters of provinces based on interconnections, i.e. neighbors
    which are connected to other neighbors at the same time, this also allows
    to define the minimum amount of senders needed to fill the map, namely
    the maximum of all interconnections found
    """

    # dictionary to keep track of all pools with clusters of certain length
    cluster_pools = {}

    # iterate over province objects
    for province in provinces:

        # iterate over all neighbors of given province
        for neighbor in provinces[province].neighbors:
            cluster_participants = [provinces[province].name, neighbor]

            # connections is by default 1 for a neighbor
            interconnections = 1

            # iterate over neighbors of the selected neighbor
            for other_neighbor in provinces[province].neighbors:

                # check if neighbor is in neighbor of in neighbors
                if other_neighbor in provinces[neighbor].neighbors:

                    # add neighbor to given cluster
                    cluster_participants.append(other_neighbor)
                    interconnections += 1

            if interconnections in cluster_pools:
                cluster_pools[interconnections].append(cluster_participants)

            else:
                cluster_pools[interconnections] = cluster_participants

    # iterates over pools
    for pool in cluster_pools:

        # iterates over clusters
        for cluster in range(len(cluster_pools[pool])):

            """
            corrects bug that wrongly puts in clusters as string instead of
            list
            """
            if isinstance(cluster_pools[pool][cluster], str):
                cluster_pools[pool][cluster] = [cluster_pools[pool][cluster]]

    # return the dictionary containing all clusters per province
    return(cluster_pools)


def state_space(provinces):
    """
    this function calculates the total state space, which is the amount of
    senders (7) to the power of the amount of provinces
    """
    all_possibilities = 1
    for i in range(len(provinces)):
        all_possibilities = all_possibilities * 7

    return all_possibilities
