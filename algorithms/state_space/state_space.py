import copy
import collections as clc


def clusters(provinces, senders, province_pools):
    """
    finds all clusters of provinces based on interconnections, i.e. neighbors
    which are connected to other neighbors at the same time, this also allows
    to define the minimum amount of senders needed to fill the map, namely
    the maximum of all interconnections found
    """

    # dictionary to keep track of all pools with clusters of certain length
    clusters = []

    # iterate over province objects
    for province in provinces:

        # iterate over all neighbors of given province
        for neighbor in provinces[province].neighbors:

            # list of clusters shared
            clusters_shared = [[province, neighbor]]

            # iterate over neighbors of the selected neighbor
            for other_neighbor in provinces[neighbor].neighbors:

                # check if neighbor shares other neighbors with this province
                if other_neighbor in provinces[province].neighbors:

                    """
                    check if other_neighbor shares all cluster_participants
                    as neighbors
                    """
                    cluster_check = []

                    # check if new cluster is necessary
                    new_cluster = True

                    """
                    check if shared neighbor can be added to an existing
                    shared cluster
                    """
                    for cluster in range(len(clusters_shared)):
                        for name in clusters_shared[cluster]:

                            # check if names appear with new shared neighbor
                            if name in provinces[other_neighbor].neighbors:
                                cluster_check.append(name)

                        # check if cluster_check matches a shared cluster
                        if sorted(clusters_shared[cluster]) == sorted(cluster_check):

                            # other_neighbor can be added to existing cluster
                            clusters_shared[cluster].append(other_neighbor)
                            new_cluster = False

                    # otherwise a new shared cluster is found
                    if new_cluster:
                        cluster_check.append(name)
                        clusters_shared.append(cluster_check)

            # adds shared clusters to total list of clusters
            for cluster in range(len(clusters_shared)):
                clusters.append(sorted(clusters_shared[cluster]))

    # create a final clusters list without duplicates
    clusters_final = []
    for cluster in range(len(clusters)):
        if not clusters[cluster] in clusters_final:
            print(clusters[cluster])
            clusters_final.append(clusters[cluster])

    print(len(clusters_final))
    clusters_final = sorted(clusters_final, reverse=True)
    return clusters_final


def lower_bound(provinces, senders, cluster_pools):
    """
    calculates the lower bound of the state space based on the maximum amount
    of interconnections encountered in a cluster
    """

    # max interconnections is contained in the keys of cluster_pools
    min_senders = sorted(cluster_pools, reverse=True)[0]

    # the amount of senders for use is based on the minimum amount needed
    for cluster in range(len(cluster_pools)):
        senders_allowed = len(cluster_pools[cluster])
        for province in cluster_pools[cluster]:
            if not provinces[province].sender_options:
                additional_constraint = 0
                for neighbor in provinces[province].neighbors:
                    if provinces[province].neighbors:
                        additional_constraint += 1
                provinces[province].sender_options = senders_allowed - additional_constraint
                senders_allowed -= 1
                if provinces[province].sender_options < 0:
                    print(provinces[province].name)
                    print()

def cluster_partipication(provinces, senders, province_pools):
    cluster_pools = clusters(provinces, senders, province_pools)
    lower_bound(provinces, senders, cluster_pools)


# def state_space(provinces, senders):
#     """
#     this function calculates the approximation of the upper and lower bounds of
#     the state space given the constraints for the assignment.
#     The upper bound is defined as the range of options possible with all 7
#     senders, whereas the lower bound is the maximum amount of combinations
#     possible under constraints with the minimum amount of senders needed based
#     on the amount of interconnections
#     """

def state_space(provinces, senders):
    """
    this function calculates the total state space, which is the amount of
    senders (7) to the power of the amount of provinces
    """
    all_possibilities = 1
    senders_amount = len(senders)
    for i in range(len(provinces)):
        all_possibilities = all_possibilities * senders_amount

    return all_possibilities

    # lower = lower_bound(provinces, senders)
    # upper = upper_bound(provinces, senders)

    # return ([lower, upper])
