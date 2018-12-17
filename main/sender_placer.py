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
import welsh_powell as welsh
from depthfirst import depth_first
import initialiser as init
import state_space as state
import checker as check

# define global variables
INPUT_CSV = 'russia_borders.csv'
PROVINCES = init.province_initialiser(INPUT_CSV)
SENDERS = init.sender_initialiser()
COMBINATIONS = 500000


if __name__ == "__main__":
    """
    loads provinces and senders and finds solutions using named
    """

    # runs depth_first
    # depth_first(PROVINCES, SENDERS, COMBINATIONS, INPUT_CSV)

    # resets senders in provinces for next run
    check.provinces_reset(PROVINCES)

    # returns pools of provinces based on number of neighbors into dictionary
    province_pools = init.neighbor_sorted_provinces(PROVINCES)
    #
    # # prints state space properties
    # print(len(state.clusters(PROVINCES, SENDERS, province_pools)))
    # print(state.mean_connections(PROVINCES))
    # print(state.cost_objective(PROVINCES, SENDERS))
    # print(state.state_space(PROVINCES, SENDERS))

    # uses the wellsh powel function to test different variations of pool sorts
    welsh.welsh_powell_variation(province_pools, PROVINCES, SENDERS, INPUT_CSV)
