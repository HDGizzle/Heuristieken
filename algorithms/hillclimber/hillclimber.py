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


def hill_climber(provinces, senders):
    """
    this function first places a sender in chart and then makes alterations
    in the hope of improvement
    """

    check.place_senders(provinces, senders)

    outcome = check.save_outcome(provinces)
    print(check.total_costs(provinces, outcome))
    # amount of changes maximally to be made is set at limit
    limit = 10

    # outcome is the state
    outcome = alteration(provinces, senders, outcome, limit)
    print(check.total_costs(provinces, outcome))

def alteration(provinces, senders, outcome, limit):
    """
    This function tries to improve the current outcome by implementing random
    alterations
    """

    types = check.types_used(outcome)

    # hillclimber can only make maximum amount of alterations
    if limit > 0:

        random.seed(limit)

        # list is used to put senders in provinces and is shuffled every time
        provinces_list = list(provinces.keys())
        random.shuffle(provinces_list)

        #  iterate over senders
        for type in types:
            for province in provinces_list:

                #  check if sender can be placed
                new_sender = True
                for neighbor in provinces[province].neighbors:
                    if type == provinces[neighbor].sender.type:
                        new_sender = False

                # places new sender if possible
                if new_sender:

                    # remove province from list to alterate
                    provinces[province].sender = senders[type]
                    provinces_list.remove(province)

        # checks if outcome is valid, if so compare against benchmark
        if check.validity_check(provinces):

            #  save new outcome and compare against benchmark
            new_outcome = check.save_outcome(provinces)
            if check.total_costs(provinces, new_outcome) < check.total_costs(provinces, outcome):
                outcome = new_outcome

        limit -= 1
        # make new alteration
        return alteration(provinces, senders, outcome, limit)

    # algoritm has made max alterations and returns best outcome
    else:
        return outcome
