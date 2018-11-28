"""
generates a class for province
elements included are:
- sender type (ranging from A to G)
- sender costs
"""


class Sender():

    # sender objects consist of type and costs
    def __init__(self, type, costs):
        self.type = type
        self.costs = costs
