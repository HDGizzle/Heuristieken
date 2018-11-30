"""
generates a class for province
elements included are:
- province name
- a list of neighbors names
- a sender object
- sender options (for state space calculation)
"""


class Province():
    """"
    province objects consist of name, neighbors list, current sender and
    senders placeable. sender placed and sender options are initialised to None
    """
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors
        self.sender = None
        self.sender_options = None

    def sender_placer(self, provinces, senders):
        """
        places senders in a province
        """

        if not self.sender:
            # check what senders are usable
            for sender in senders:

                # defines whether sender is usable
                usable = True

                # checks senders type for other neighbors
                for neighbor in self.neighbors:

                    # if sender is with neighbor, sender cannot be used
                    if provinces[neighbor].sender:
                        if sender == provinces[neighbor].sender.type:
                            usable = False

                # places sender if usable
                if usable:
                    self.sender = senders[sender]
                    break
