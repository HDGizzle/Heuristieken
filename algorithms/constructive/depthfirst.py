import os
import sys
import math
basepath = os.path.abspath(os.path.curdir).split("Heuristieken")[0] + "Heuristieken"
sys.path.append(os.path.join(basepath, "main"))
sys.path.append(os.path.join(basepath, "visualiser"))
import outcome_plotter
import checker as check
import random
from collections import defaultdict


def low_variance_picker(possible, usage):
    """
    sorts dictionary of senders based on the frequency of their respective
    usage, which leads to a more even distribution of sender types by given
    preference to the sender with the lowest frequency in placing it
    """
    for sendtype, used in sorted(usage.items(), key=lambda x: x[1]):
        if sendtype in possible:
            return sendtype
    if possible:
        return possible[0]
    else:
        # outcome will not be valid, but also not saved, because validity check
        # is used
        return 1


def depth_first(provinces, senders, combinations):
    """
    depth first is used to try out a given amount of combinations and finds
    outcomes with either the lowest variance or costs
    """

    # places senders in provinces and uses outcome as benchmark
    check.place_senders(provinces, senders)
    benchmark = check.save_outcome(provinces)

    # collect data for frequency histograms
    variances = []
    costs = []

    # try n combinations
    for i in range(combinations):

        """
        define a controlled random in order to roam statespace and make search
        replicable
        """
        random.seed(i)

        # define visited as empty set
        visited = set()

        # clear senders from provinces
        check.provinces_reset(provinces)

        # pick first province to start with
        stack = [list(provinces.keys())[0]]

        # this dictionary keeps track of sender usage
        usage = defaultdict(int)

        # assign sendertype to provinces without neighbors
        for province in provinces:
            if not provinces[province].neighbors:
                provinces[province].sender_placer(provinces, senders)
                usage[provinces[province].sender.type] += 1
                visited.add(province)

        # as long as stack contains provinces
        while stack:
            province = stack.pop()

            # start on top of loop if province has already been visited
            if province in visited:
                continue

            # append current province to visited
            visited.add(province)

            # define unvisited neighbors list
            neighbors = []
            for neighbor in provinces[province].neighbors:
                if neighbor not in visited:
                    neighbors.append(neighbor)

            # add all unvisited neighbors to stack and shuffle order
            random.shuffle(neighbors)
            stack.extend(neighbors)

            # define sendtypes
            sender_types = list(senders.keys())

            # remove senders already used with neighbors
            for neighbor in provinces[province].neighbors:
                if provinces[neighbor].sender:
                    if provinces[neighbor].sender.type in sender_types:
                        sender_types.remove(provinces[neighbor].sender.type)

            # assign available sender type based on usage
            sender = low_variance_picker(sender_types, usage)
            provinces[province].sender = senders[sender]
            usage[sender] += 1


        # keep track of outcome
        outcome = check.save_outcome(provinces)

        costs.append(check.advanced_costs(senders, outcome))
        # variances.append(math.sqrt(check.sender_variance(outcome)))


        # check if outcome is more efficient than benchmark
        if check.validity_check(provinces):
            if check.enhanced_distribution(outcome, benchmark):
                benchmark = outcome
                seed = i
                bestusage = usage

    print(benchmark)
    print(bestusage)
    print("Best Variance Seed:", seed)
    print("Best Variance Frequencies:", bestusage)
    outcome_plotter.plotter(costs, "Costs", "results/costsadvUkraine.png", combinations)
    # outcome_plotter.plotter(costs, "costs", "costplot.png")
