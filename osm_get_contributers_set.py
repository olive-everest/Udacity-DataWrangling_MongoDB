#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def get_user(element):
    #get user attribute values for 'node', 'way' and 'relation' tags
    if (element.tag == 'node' or element.tag == 'way' or element.tag == 'relation') :
        user = element.attrib['user']
        #print user
        return user


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        users.add(get_user(element))
    return users - set([None])      # Get rid of None from the set


def test():

    users = process_map('example.osm')
    pprint.pprint(users)
    assert len(users) == 6



if __name__ == "__main__":
    test()

"""
Results:
set(['Umbugbene',
     'bbmiller',
     'fredr',
     'linuxUser16',
     'uboot',
     'woodpeck_fixbot'])
"""
