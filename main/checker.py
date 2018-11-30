"""
this file provides functions to see if the senders are placed correctly and
calculates the total amount of money used for the solution
"""


def province_reset(provinces):
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


def sender_checker(provinces):
    """
    checks if outcome is valid by checking senders on constraints
    """

    # determines validity of outcome
    valid = True

    # iterate over provinces
    for province in provinces:

        # check if neighbor has same sendertype and senders are placed
        for neighbor in provinces[province].neighbors:
            if provinces[neighbor].sender == provinces[province].sender:
                valid = False

            elif not provinces[neighbor].sender:
                valid = False

    # returns the outcome of the check
    return valid


def cost_calculator(outcome, senders):
    """
    calculates the total costs based on cost of senders used
    """

    costs = 0
    for province in outcome:
        sender_used = outcome[province]
        costs += senders[sender_used].costs

    return costs


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
    return sendertypes_used
