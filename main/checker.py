"""
this file provides functions to see if the senders are placed correctly and
calculates the total amount of money used for the solution
"""


def provinces_reset(provinces):
    """
    takes all senders in the provinces away
    """

    for province in provinces:
        provinces[province].sender = None


def save_outcome(provinces):
    """
    saves the outcome with the provinces and senders placed
    """
    outcome = {}
    for province in provinces:
        outcome[province] = provinces[province].sender.type

    return outcome


def validity_check(provinces):
    """
    checks if outcome is valid by checking senders on constraints
    """

    # determines validity of outcome
    valid = True

    # iterate over provinces
    for province in provinces:

        # guard for lacking sender in province
        if provinces[province].sender:

            # check if neighbor has same sendertype and senders are placed
            for neighbor in provinces[province].neighbors:

                # guard for lacking sender in province
                if provinces[neighbor].sender:

                    if provinces[neighbor].sender == provinces[province].sender:
                        valid = False

                # sender missing, no valid outcome
                else:
                    valid = False
                    return valid

        # sender missing, no valid outcome
        else:
            valid = False
            return valid

    # returns the outcome of the check
    return valid


def place_senders(provinces, senders):
    """
    places senders in provinces
    """
    for province in provinces:
        provinces[province].sender_placer(provinces, senders)


def senders_placed(outcome):
    """
    keeps track of all senders placed and their frequency
    """

    senders_used = []
    for province in outcome:
        senders_used.append(outcome[province])
    return senders_used


def types_used(outcome):
    """
    returns list of which senders used
    """

    sendertypes_used = []
    for province in outcome:
        if not outcome[province] in sendertypes_used:
            sendertypes_used.append(outcome[province])
    return sorted(sendertypes_used)


def sender_variance(new_outcome):
    """
    keeps track of how evenly distributed senders are senders_placed by
    calculating the variance of sender occurrences
    """

    variance = 0
    placed_senders = senders_placed(new_outcome)
    types = types_used(new_outcome)
    mean_freq = len(placed_senders) / len(types)

    # calculates the  variance of occurrences in senders
    for sender in types:
        freq_sender = placed_senders.count(sender)
        variance += (freq_sender - mean_freq) * (freq_sender - mean_freq)

    return variance


def enhanced_distribution(outcome, benchmark_outcome):
    """
    checks if new outcome has better sender distribution and less senders
    used than currently measured best outcome
    """

    # checks if outcome is better than benchmark
    better_outcome = False

    # obtains sender types used and variances
    used = len(types_used(outcome))
    benchmark_used = len(types_used(benchmark_outcome))
    current_var = sender_variance(outcome)
    benchmark_var = sender_variance(benchmark_outcome)

    # checks if senders used does not exceed benchmark
    if not used > benchmark_used:

        # outcome is better with less senders used or lower variance
        if used < benchmark_used or current_var < benchmark_var:
            better_outcome = True

    return better_outcome


def total_costs(senders, outcome):
    """
    calculates the lowest costs an outcome generate given all 4 cost schemes
    and returns the lowest total costs it can find
    """
    costs = []
    for i in range(4):
        all_costs = 0
        for province in outcome:
            all_costs += senders[outcome[province]].costs[i]
        costs.append(all_costs)
    return min(costs)


def advanced_costs(senders, outcome):
    """
    this function retrieves the lowest costs under the advanced cost scheme
    """
    # keep track of costs and retrieve types used and senders placed
    costs = []
    placed = senders_placed(outcome)
    types = types_used(outcome)

    # iterate over four costs schemes
    for i in range(4):

        # costs start at 0
        all_costs = 0

        # iterate over specific sender types used
        for type in types:

            # calculate the amount of the sender type used
            amount = placed.count(type)

            # price index starts at 100% of initital price
            index = 1

            # iterate over the amount of senders used
            for j in range(amount):

                # after the first sender every next sender becomes 10% cheaper
                if j > 0:
                    index = index * 0.9
                all_costs += index * senders[type].costs[i]

        # add total costs to list
        costs.append(all_costs)

    # returns minimum of costs
    return min(costs)


def lower_costs(senders, outcome, benchmark):
    """
    this function tests whether a given outcome can give lower costs under
    any of the 4 cost schemes compared to its benchmark
    """
    if total_costs(senders, outcome) < total_costs(senders, benchmark):
        return True
    else:
        return False


def lower_adv_costs(senders, outcome, benchmark):
    """
    this function tests whether a given outcome can give lower advanced
    costs under any of the 4 cost schemes compared to its benchmark
    """
    if advanced_costs(senders, outcome) < advanced_costs(senders, benchmark):
        return True
    else:
        return False


def cost_scheme(provinces, outcome):
    """
    retrieves the respective cost scheme
    """
    lowest_cost = total_costs(provinces, outcome)
    for i in range(4):
        all_costs = 0
        for province in outcome:
            all_costs += provinces[province].sender.costs[i]
        # if costs tested matches cost scheme return cost scheme
        if all_costs == lowest_cost:
            return i + 1
