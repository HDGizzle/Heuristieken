"""
this script places senders in different provinces under the constraint that
bordering provinces cannot have the same sender type
"""

# imports files and functions
from welsh_powell import welsh_powell_variation
import initializer as init

# define global variables
INPUT_CSV = 'nederland.csv'
PROVINCES = init.province_initialiser(INPUT_CSV)
SENDERS = init.sender_initialiser()


if __name__ == "__main__":
    """
    loads provinces and senders and finds optimal solution using algoritm
    """

    # returns pools of provinces based on number of neighbors into dictionary
    province_pools = init.neighbor_sorted_provinces(PROVINCES)

    # uses the wellsh powel function to test different variations of pool sorts
    welsh_powell_variation(province_pools, PROVINCES, SENDERS)
