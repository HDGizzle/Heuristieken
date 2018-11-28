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

                    # check if other_neighbor fits with cluster_participants
                    cluster_check = []
                    new_cluster = True

                    # check if shared neighbor can be added to a shared cluster
                    for cluster in range(len(clusters_shared)):
                        for name in clusters_shared[cluster]:

                            # check if names appear with new shared neighbor
                            if name in provinces[other_neighbor].neighbors:
                                cluster_check.append(name)

                        # check if cluster_check matches a shared clusters
                        if sorted(clusters_shared[cluster]) == sorted(cluster_check):

                            # if so other_neighbor can be added to existing cluster
                            clusters_shared[cluster].append(other_neighbor)
                            new_cluster = False

                    # if cluster check did not match an existing, new cluster is necessary
                    if new_cluster:
                        cluster_check.append(name)
                        clusters_shared.append(cluster_check)

            # adds shared clusters to total list of clusters
            for cluster in range(len(clusters_shared)):
                clusters.append(sorted(clusters_shared[cluster]))

    # clusters final contain no duplicates
    clusters_final = []
    for cluster in range(len(clusters)):
        if not clusters[cluster] in clusters_final:
            print(clusters[cluster])
            clusters_final.append(clusters[cluster])

    clusters_final = sorted(clusters_final, reverse=True)
    print(len(clusters_final))
    return clusters_final


# def lower_bound(provinces, senders):
#     """
#     calculates the lower bound of the state space based on the maximum amount
#     of interconnections encountered in a cluster
#     """
#
#     # max interconnections is contained in the keys of cluster_pools
#     cluster_pools = clusters(provinces)
#     min_senders = sorted(cluster_pools, reverse=True)[0]
#
#     # the amount of senders for use is based on the minimum amount needed
#     senders_available = {}
#     for type in senders:
#
#         # adds senders to sender available based on amount needed
#         if type <= min_senders:
#             senders_available[type] = senders[type]
#
#     # iterate over provinces in pools starting at highest interconnections
#     for pool in sorted(cluster_pools, reverse=True):
#         for cluster in cluster_pools[pool]:
#             for province in cluster_pools[pool][cluster]:
#
#                 # check if amount of options is already assigned
#                 if not provinces[province].sender_options:
#
#                     # options available are is dependent on amount available
#                     options = min_senders


def cluster_partipication(provinces, senders, province_pools):
    cluster_pools = clusters(provinces, senders, province_pools)


def state_space(provinces, senders):
    """
    this function calculates the approximation of the upper and lower bounds of
    the state space given the constraints for the assignment.
    The upper bound is defined as the range of options possible with all 7
    senders, whereas the lower bound is the maximum amount of combinations
    possible under constraints with the minimum amount of senders needed based
    on the amount of interconnections
    """

    # lower = lower_bound(provinces, senders)
    # upper = upper_bound(provinces, senders)

    # return ([lower, upper])
