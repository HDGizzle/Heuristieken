"""
this script places senders in different provinces under the constraint that
bordering provinces cannot have the same sender type
"""

# imports files and functions
import os
import sys
basepath = os.path.abspath(os.path.curdir).split("Heuristieken")[0] + "Heuristieken"
sys.path.append(os.path.join(basepath, "algorithms", "greedy"))
sys.path.append(os.path.join(basepath, "algorithms", "constructive"))
sys.path.append(os.path.join(basepath, "algorithms", "hillclimber"))
sys.path.append(os.path.join(basepath, "algorithms", "state_space"))
sys.path.append(os.path.join(basepath, "initialiser"))
from welsh_powell import welsh_powell_variation
from depthfirst import depth_first
import initialiser as init
import state_space as state

# define global variables
INPUT_CSV = 'usa_borders.csv'
PROVINCES = init.province_initialiser(INPUT_CSV)
SENDERS = init.sender_initialiser()


if __name__ == "__main__":
    """
    loads provinces and senders and finds solutions using named
    """

    # returns pools of provinces based on number of neighbors into dictionary
    # province_pools = init.neighbor_sorted_provinces(PROVINCES)

    # calculates the state space for a given map
    # state.cluster_partipication(PROVINCES, SENDERS, province_pools)
    # lower_bound(PROVINCES, SENDERS)
    # state_space(PROVINCES, SENDERS)

    # uses the wellsh powel function to test different variations of pool sorts

    # welsh_powell_variation(province_pools, PROVINCES, SENDERS)
    depth_first(PROVINCES, SENDERS, 2000000)





    def total_costs(provinces):
        costs = 0
        for province in provinces:
            costs += provinces[province].sender.costs

        print(costs)
