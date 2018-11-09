"""
generates a class for province
elements included are:
- province name
- a list of neighbors names
- a sender object
"""

class Province(object):

    # province objects consist of name, neighbors list and sender
    # senders are initialised to None
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors
        self.sender = None
