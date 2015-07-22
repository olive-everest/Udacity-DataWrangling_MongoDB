#!/usr/bin/env python
# -*- coding: utf-8 -*-
# All your changes should be in the 'extract_airports' function
# It should return a list of airport codes, excluding any combinations like "All"

from bs4 import BeautifulSoup
import re
html_page = "options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        soup = BeautifulSoup(html)
        s1 = soup.find(id = 'AirportList')
        s2 = s1.find_all('option')
        for entry in s2:
            airport_code = entry['value']
            if (re.match('All', airport_code)) :
                continue
            data.append(airport_code)
    return data


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

test()
