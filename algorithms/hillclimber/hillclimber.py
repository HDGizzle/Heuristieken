"""
hill climber uses a solution and makes alterations until a better position is
found. This then becomes the default position and alterations are again made
untill no better solution can be found within specified time limit
"""

# libraries to import
import os
import sys
import random

#  import paths
basepath = os.path.abspath(os.path.curdir).split("Heuristieken")[0] + \
        "Heuristieken"
sys.path.append(os.path.join(basepath, "main"))

# additional functions to import
import checker as check

# maximum amount that map can be changed
LIMIT = 100


def hill_climber(provinces, senders, outcome):
    """
    this function is allowed to check the map N times as specified under LIMIT.
    If the alteration finds a better solution within limit, the function is
    rerun. If no better solution is found, then the function returns the best
    found outcome
    """
    # print best outcome after given alterations have been made
    outcome = alteration(provinces, senders, outcome)
    return outcome


def alteration(provinces, senders, benchmark):
    """
    This function tries to improve the current outcome by implementing
    alterations
    """
    #  save sender types to use
    types = check.types_used(benchmark)

    # start value for i, in first run initialised at 0
    i = 0

    # hillclimber can only make maximum amount of alterations
    while i < LIMIT:

        # list is used to put senders in provinces and is shuffled every time
        provinces_list = list(provinces.keys())
        random.shuffle(provinces_list)

        # iterate over senders
        for type in types:
            for province in provinces_list:

                #  check if sender can be placed
                new_sender = True

                # check if sender is usable
                for neighbor in provinces[province].neighbors:
                    if type == provinces[neighbor].sender.type:
                        new_sender = False

                # places new sender if possible
                if new_sender:

                    # remove province from list to alterate
                    provinces[province].sender = senders[type]
                    provinces_list.remove(province)

                    #  save new outcome and compare against benchmark
                    new_outcome = check.save_outcome(provinces)

                    if check.lower_costs(senders, new_outcome, benchmark):
                        benchmark = check.save_outcome(provinces)

                        # hill climber should restart from new benchmark
                        return alteration(provinces, senders, benchmark)

        # iteration has been made
        i += 1

    # algorithm has made max alterations and returns best outcome
    return benchmark
