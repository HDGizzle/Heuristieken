"""
this script places senders in different provinces under the constraint that
bordering provinces cannot have the same sender type
"""

# imports files and functions
from welsh_powell import welsh_powell_variation
import initializer as init
from state_space import state_space

# define global variables
INPUT_CSV = 'usa_borders.csv'
PROVINCES = init.province_initialiser(INPUT_CSV)
SENDERS = init.sender_initialiser()


if __name__ == "__main__":
    """
    loads provinces and senders and finds solutions using named
    """

    # returns pools of provinces based on number of neighbors into dictionary
    province_pools = init.neighbor_sorted_provinces(PROVINCES)

    # calculates the state space for a given map
    state_space(PROVINCES)

    # uses the wellsh powel function to test different variations of pool sorts
    welsh_powell_variation(province_pools, PROVINCES, SENDERS)
