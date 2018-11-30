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
            clusters_final.append(clusters[cluster])

    clusters_final = sorted(clusters_final, reverse=True)
    return clusters_final


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
