#!/usr/bin/env python
# Name: Jan Peters
# Student number: 10452125
"""
this script scrapes data on Russia oblasts and borders
"""

# imports libraries
import os
import sys
basepath = os.path.abspath(os.path.curdir).split("Heuristieken")[0] + "Heuristieken"
sys.path.append(os.path.join(basepath, "main", "objects"))
import csv
from province_class import Province
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

TARGET_URL = "https://en.wikipedia.org/wiki/Borders_of_Russia"
OUTPUT_CSV = 'russia_borders.csv'


def extract_provinces(dom):
    """
    extract all relevant oblast information on htmlpage
    """

    # saves the tables containing provinces and neighbors
    tables = dom.find_all("div", {"class":"div-col columns column-width"})

    # dictionary to hold all oblasts objects
    all_oblasts = {}

    # iterates over all tables on page
    for table in tables:

        # finds all provinces in table
        provinces = table.find_all("p")

        # list to contain all neighbors in Russia to province
        russian_neighbors = []

        # iterates over all neighbors to province
        all_neighbors = table.find_all("li")
        for neighbor in all_neighbors:

            # adds all Russian neighbors to list
            if "Russia" in neighbor.text:

                # extracts all names from Russian all_neighbors
                names = neighbor.find_all("a")

                # adds list for names of Russian neighbors from provinces
                russian_neighbors.append([])

                # adds names to list in Russian neighbors
                for name in names:
                    if not name == 'Khabarovsk Krai':
                        russian_neighbors[-1].append(name.string)

            # Kaliningrad has no Russian borders and is an enclave
            elif "Poland" in neighbor.text:
                russian_neighbors.append([])

        # generates new province objects and adds it to dictionary
        new_provinces = len(provinces)

        # iterates over existing oblasts and respective neighbors
        for i in range(new_provinces):

            # adds only oblasts to dictionary
            province = Province(provinces[i].text, russian_neighbors[i])
            all_oblasts[provinces[i].text] = province

    # returns list of oblasts
    return all_oblasts


def save_csv(outfile, provinces):
    """
    output a CSV file containing provinces, neighbors and init sender
    """
    writer = csv.writer(outfile)

    # write header
    writer.writerow(["name", "neighbors"])

    # provinces list contain all provinces information in lists
    provinces_list = []
    neighbors = ", "

    # iterates over objects in dictionary
    for key in provinces:

        # stores object elements information in list
        province = provinces[key]
        provinces_list.append([province.name, neighbors.join(province.neighbors)])

    # write province info to file
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

    # extract the oblasts and neighbors
    provinces = extract_provinces(dom)

    # write the CSV file to disk (including a header)
    with open(OUTPUT_CSV, 'w', newline='') as output_file:
        save_csv(output_file, provinces)
