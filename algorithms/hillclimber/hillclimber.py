"""
hill climber randomly generates a solution and starts optimizing for colors
or cash used
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

# maximum amount of that provinces may be checked for alteration
LIMIT = 10000


def hill_climber(provinces, senders):
    """
    this function first places a sender in chart and then makes alterations
    in the hope of improvement
    """

    # place senders and show results for initial outcome
    check.place_senders(provinces, senders)
    outcome = check.save_outcome(provinces)
    print(check.advanced_costs(senders, outcome))

    # print best outcome after given alterations have been made
    outcome = alteration(provinces, senders, outcome, LIMIT)
    print(check.advanced_costs(senders, outcome))


def alteration(provinces, senders, benchmark, limit):
    """
    This function tries to improve the current outcome by implementing
    alterations
    """
    #  save sender types to use
    types = check.types_used(benchmark)

    # start value for i, in first run initialised at 0
    i = LIMIT - limit

    # hillclimber can only make maximum amount of alterations
    while i < LIMIT:

        # limit is used to seed random
        random.seed(i)

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
                    if check.lower_adv_costs(senders, new_outcome, benchmark):
                        benchmark = check.save_outcome(provinces)

                        # runs left to make used for next i initialisation
                        runs = LIMIT - i

                        # hill climber should restart from new benchmark
                        return alteration(provinces, senders, benchmark, runs)

        # iteration has been made
        i += 1

    # algoritm has made max alterations and returns best outcome
    return benchmark
