#!/usr/bin/env python
# Name: Jan Peters
# Student number: 10452125
"""
this script scrapes data on USA states and borders
"""

# imports libraries
import re
import csv
from province_class import Province
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

TARGET_URL = "https://state.1keydata.com/bordering-states-list.php"
OUTPUT_CSV = 'usa_borders.csv'


def extract_provinces(dom):
    """
    extract all relevant movie information on htmlpage
    """
    # parse the HTML file into a DOM representation
    tables = dom.find_all("table", {"class":"content4"})
    rows = tables[0].find_all("tr")
    rows.pop(0)

    # creates a dictionary to contain all province objects
    provinces = {}

    # iterates over rows in table containing province info
    for row in rows:
        columns = row.find_all("td")

        # first column contains state, second contains neighbors
        name = columns[0].string

        # neighbors are saved in a list
        neighbors = columns[1].string.split(", ")

        # sender is initialised to one
        sender = 1

        # creates province object and adds it to dictionary
        province = Province(name, neighbors, sender)
        provinces[name] = province

    # returns dictionary of provinces
    return provinces


def save_csv(outfile, provinces):
    """
    output a CSV file containing provinces, neighbors and init sender
    """
    writer = csv.writer(outfile)

    writer.writerow(["name", "neighbors", "sender"])
    provinces_list = []
    neighbors = ", "

    for key in provinces:
        province = provinces[key]
        provinces_list.append([province.name, \
                    neighbors.join(province.neighbors), province.sender])

    writer.writerows(provinces_list)


def simple_get(url):
    """
    attempts to get the content at `url` by making an HTTP GET request.
    if the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        print('The following error occurred during HTTP GET request to\
                0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    returns true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


if __name__ == "__main__":
    # get HTML content at target URL
    html = simple_get(TARGET_URL)

    # extract info from HTML page
    dom = BeautifulSoup(html, 'html.parser')

    # extract the states and neighbors
    provinces = extract_provinces(dom)

    # write the CSV file to disk (including a header)
    with open(OUTPUT_CSV, 'w', newline='') as output_file:
        save_csv(output_file, provinces)
