"""
this script places senders in different provinces under the constraint that
bordering provinces cannot have the same sender type
"""

# imports libraries
import pandas
import csv
from province_class import Province
from sender_class import Sender

# define global variables
SENDERS = {}
PROVINCES = {}
INPUT_CSV = "usa_borders.csv"

def sender_initialiser():
    """
    initializes seven sendertypes and adds them to global dictionary
    """

    # sender types range from A-G
    sender_types = ["ABCDEFG"]

    # for first project sender costs are initialised to zero
    costs = 0

    # adds all different sender type objects to SENDERS
    for char in sender_types:
        SENDERS[char] = Sender(char, costs)

def province_initialiser():
    """
    initializes all province objects and adds them global dictionary
    provinces are imported from csv files
    """

    # opens csv file containing province data
    with open(INPUT_CSV) as myfile:
        datafile = pandas.read_csv(myfile)

        # iterates over rows in csv file
        for i in range(len(datafile)):

            # extracts province name and neighbors as a list
            name = datafile["name"][i]
            neighbors = str(datafile["neighbors"][i]).split(", ")

            # replaces pandas designation 'nan' for empty with empty list
            if neighbors[0] in "nan":
                neighbors = []

            # adds new province object to PROVINCES
            PROVINCES[name] = Province(name, neighbors)

def welsh_powell():
    """
    this function uses the Welsh Powell algoritm to find a solution for the
    placing of senders in provinces under color graphing constraints
    """

if __name__ == "__main__":
    """
    loads provinces and senders and finds optimal solution using algoritm
    """
    # initializes all senders and adds them to SENDERS
    sender_initialiser()

    # initializes all province objects and adds them to PROVINCES
    province_initialiser()

    sender
