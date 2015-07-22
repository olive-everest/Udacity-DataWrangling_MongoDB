#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI
# All your changes should be in the 'extract_carrier' function
# Also note that the html file is a stripped down version of what is actually on the website.

# Your task in this exercise is to get a list of all airlines. Exclude all of the combination
# values, like "All U.S. Carriers" from the data that you return.
# You should return a list of codes for the carriers.

from bs4 import BeautifulSoup
import re
html_page = "options.html"


def extract_carriers(page):
    data = []

    with open(page, "r") as html:
        # Parse the Beautiful Soup tree until we reach the leaf
        soup = BeautifulSoup(html)
        # First, zoom into the section of the page that we care about
        s1 = soup.find(id='CarrierList')
        # Second, filter out only the 'option' leaves
        s2 = s1.find_all('option')
        # Third, extract all the values in this list (now at a leaf node)
        for entry in s2 : 
            code = entry['value']
            #print code
            # Discard any codes that begin with 'All', else append to data
            if (re.match('All', code)) :
                continue
            data.append(code)
    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]
    airport = data["airport"]
    carrier = data["carrier"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': airport,
                          'CarrierList': carrier,
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })

    return r.text


def test():
    data = extract_carriers(html_page)
    assert len(data) == 16
    assert "FL" in data
    assert "NK" in data

test()
