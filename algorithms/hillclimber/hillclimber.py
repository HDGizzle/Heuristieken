"""
hill climber randomly generates a solution and starts optimizing for colors
or cash used
"""

# libraries to import
import os
import sys

#  import paths
basepath = os.path.abspath(os.path.curdir).split("Heuristieken")[0] + \
        "Heuristieken"
sys.path.append(os.path.join(basepath, "main"))

# additional functions to import
import checker as check


def hill_climber(provinces, senders):
    """
    this function first randomly fills a chart and then starts improving
    """

    check.place_sender(provinces, senders)

    outcome = check.save_outcome(provinces)
    print(check.sender_variance(outcome))

    change = 0
    limit = 900
    outcome = alteration(provinces, senders, outcome, change, limit)


def alteration(provinces, senders, outcome, changes, limit):
    """
    This function tries to improve the current outcome by implementing random
    alterations
    """

    # list is used to put senders in provinces
    provinces_list = list(provinces.keys())

    alteration_made = False
    if changes < limit:

        for sender_type in senders:
            for province in provinces_list:
                new_sender = True
                for neighbor in provinces[province].neighbors:
                    if sender_type == provinces[neighbor].sender.type:
                        new_sender = False

                # places random new senders
                if new_sender:
                    alteration_made = True
                    # print(sender_type)
                    provinces[province].sender = senders[sender_type]
                    provinces_list.remove(province)

        if not alteration_made:
            highest_sender = check.types_used(provinces)[0]

            for province in provinces:
                if provinces[province].sender.type == highest_sender:
                    provinces[province].sender.type == senders[1]

        if check.validity_check(provinces):

            new_outcome = check.save_outcome(provinces)
            # print(check.sender_variance(new_outcome))
            if check.enhanced_distribution(new_outcome, outcome):
                outcome = new_outcome
            changes += 1
        return alteration(provinces, senders, outcome, changes, limit)

    else:
        print(check.sender_variance(outcome))
        return outcome
