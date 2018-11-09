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
INPUT_CSV = "nederland.csv"

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
    with open(INPUT_CSV) as myfile:
        datafile = pandas.read_csv(myfile)
        # iterates over row and saves data to global dictionary
        print(datafile.dtypes)
        print(datafile.index)
        print(datafile.values)
        print(datafile.columns)
        print(datafile.describe())
        print(datafile)



if __name__ == "__main__":
    # initializes all senders and adds them to SENDERS
    sender_initialiser()

    # initializes all province objects and adds them to PROVINCES
    province_initialiser()
