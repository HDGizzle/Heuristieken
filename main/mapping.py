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
sys.path.append(os.path.join(basepath, "main", "shapefiles"))
sys.path.append(os.path.join(basepath, "visualiser", "shapefiles"))
import matplotlib
if sys.platform == "darwin":
    matplotlib.use('TkAgg')
from welsh_powell import welsh_powell_variation
from depthfirst import depth_first
import initialiser as init
import state_space as state
from usa_vis import mapplotterUSA
from ukr_vis import mapplotterUKR
from russia_vis import mapplotterRUSSIA
from china_vis import mapplotterCHINA


# define global variables
INPUT_CSV = 'china_borders.csv'
PROVINCES = init.province_initialiser(INPUT_CSV)
SENDERS = init.sender_initialiser()


if __name__ == "__main__":
    """
    loads provinces and senders and finds solutions using named
    """

    # returns pools of provinces based on number of neighbors into dictionary
    province_pools = init.neighbor_sorted_provinces(PROVINCES)

    # calculates the state space for a given map
    # state.cluster_partipication(PROVINCES, SENDERS, province_pools)
    # lower_bound(PROVINCES, SENDERS)
    # state_space(PROVINCES, SENDERS)

    # WELSH POWELL
    # uses the wellsh powel function to test different variations of pool sorts
    # the [0] refers to the the outcome when welsh powell is run based on their
    # benchmark outcome. [1] is the outcome when focused on the
    # benchmark variance
    benchmark = welsh_powell_variation(province_pools, PROVINCES, SENDERS, INPUT_CSV)
    mapplotterUKR(benchmark[0])
    mapplotterUKR(benchmark[1])
    mapplotterUSA(benchmark[0])
    mapplotterUSA(benchmark[1])
    mapplotterCHINA(benchmark[0])
    mapplotterCHINA(benchmark[1])
    mapplotterRUSSIA(benchmark[0])
    mapplotterRUSSIA(benchmark[1])
    
    # DEPTH FIRST
    # uses depth first to test the different variations in sender placing
    benchmark = depth_first(PROVINCES, SENDERS, 10000)
    # Select the maplotter of the land the you have chosen for INPUT_CSV to
    # show the colored map belonging to the data.
    mapplotterUKR(benchmark)
    mapplotterUSA(benchmark)
    mapplotterCHINA(benchmark)
    mapplotterRUSSIA(benchmark)

    def total_costs(provinces):
        costs = 0
        for province in provinces:
            costs += provinces[province].sender.costs

        print(costs)
