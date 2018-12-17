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
import hillclimber as hill
from depthfirst import depth_first
import initialiser as init
import state_space as state
import checker as check

# define global variables
INPUT_CSV = 'ukraine_borders.csv'
PROVINCES = init.province_initialiser(INPUT_CSV)
SENDERS = init.sender_initialiser()
COMBINATIONS = 10000


if __name__ == "__main__":
    """
    loads provinces and senders and finds solutions using depth first,
    welsh powell and hill climber, which is used to enhance other outcomes
    """
    # runs depth_first
    """
    user can use two functions, low_variance_picker or low_cost_picker
    depending on whether optimized variance or optimized costs are the goal
    """
    depth_first(PROVINCES, SENDERS, COMBINATIONS, INPUT_CSV)

    # resets senders in provinces for next run
    check.provinces_reset(PROVINCES)

    # returns pools of provinces based on number of neighbors into dictionary
    province_pools = init.neighbor_sorted_provinces(PROVINCES)

    # prints state space properties
    print(f" CLUSTERS: {len(state.clusters(PROVINCES, SENDERS, province_pools))}")
    print(f" MEAN CONNECTIONS: {state.mean_connections(PROVINCES)} ")
    print(f" COST OBJECTIVE: {state.cost_objective(PROVINCES, SENDERS)}")
    print(f" STATE SPACE: {state.state_space(PROVINCES, SENDERS)}")

    # uses the wellsh powel function to test different variations of pool sorts
    outcomes = welsh.welsh_powell_variation(province_pools, PROVINCES,
                                            SENDERS, INPUT_CSV)

    """
    user must update hillclimber to enhanced distribution or lower cost
    depending on whether you want to enhance variance or cost outcome
    """
    cost_outcome = outcomes[0]
    variance_outcome = outcomes[1]

    # try to enhance costs using hill climber
    check.outcome_replication(PROVINCES, SENDERS, cost_outcome)
    outcome = hill.hill_climber(PROVINCES, SENDERS, cost_outcome)

    # if hillclimber has return enhanced outcome, this is printed
    if outcome != cost_outcome:
        print(outcome)
