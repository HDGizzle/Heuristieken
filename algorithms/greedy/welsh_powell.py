"""
this function uses the Welsh Powell algorithm to find a solution for the
placing of senders in provinces under color graphing constraints
http://mrsleblancsmath.pbworks.com/w/file/fetch/46119304/vertex%20coloring%20algorithm.pdf
"""

# import other classes
import os
import sys
basepath = os.path.abspath(os.path.curdir).split("Heuristieken")[0] + "Heuristieken"
sys.path.append(os.path.join(basepath, "main"))
import checker as check


def welsh_powell(province_pools, provinces, senders):
    """
    places senders first in provinces with most connections working as a greedy
    algorithm
    """

    # clear senders
    check.provinces_reset(provinces)

    # lists all numbers of connections from high to low
    connections = sorted(province_pools, reverse=True)

    # iterates over senders
    for sender in senders:

        # iterates over province pools
        for connection in connections:

            # iterates over provinces in province pools
            province_pool = province_pools[connection]
            for province_name in province_pool:

                # extracts province object
                province = provinces[province_name]

                # check for presence of sender in neighbor
                present = False

                # iterate over neighbors
                for neighbor in province.neighbors:

                    # check if sender neighbor corresponds to current sender
                    if provinces[neighbor].sender:
                        if provinces[neighbor].sender.type == sender:
                            present = True

                # place sender if sender is not in neighbors
                if not present and not province.sender:

                    # place sender
                    province.sender = senders[sender]


def welsh_powell_variation(province_pools, provinces, senders):
    """
    uses a dictionary containing pools of provinces with the same amount of
    neighbors and sorts the contents of the pool by shifting each province one
    place in the list to use varying orders for the wellsh powell algorithm.
    the total amount of variations created equals the number of provinces in
    each province pool multiplied by the other numbers of provinces in the
    other pool
    """

    # places senders in provinces and uses outcome as benchmark
    check.place_senders(provinces, senders)
    benchmark_variance = check.save_outcome(provinces)
    benchmark_costs = benchmark_variance

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

        # creates a variation of province pools
        variation_prov_pool = {}

        for counter, pool in enumerate(province_pools):
            variation_prov_pool[pool] = pool_sorts[pool][list_cursor[counter]]

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
        welsh_powell(variation_prov_pool, provinces, senders)

        # save outcome and see if it generates lower costs or variance
        outcome = check.save_outcome(provinces)

        if check.lower_costs(senders, outcome, benchmark_costs):
            benchmark_costs = outcome

        if check.enhanced_distribution(outcome, benchmark_variance):
            benchmark_variance = outcome

    return benchmark_costs, benchmark_variance
