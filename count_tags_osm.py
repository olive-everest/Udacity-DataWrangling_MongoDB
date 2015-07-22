#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
Fill out the count_tags function. It should return a dictionary with the 
tag name as the key and number of times this tag can be encountered in 
the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
    tag_dict = {}
    count = 0
		"""
		- Note that we use iterparse() when XML file is too large to be stored in memory
		- In case of the OSM Chicago maps data, the XML file is ~2Gigs, so no way we can work with this in memory
		"""
    for event, element in ET.iterparse(filename):
        #print("%s, %4s, %s" % (event, element.tag, element.text))
        # count the tags
        tag = element.tag
        if (tag in tag_dict.keys()) :
            tag_dict[tag] = tag_dict[tag] + 1
        else :
            tag_dict[tag] = 1
    return tag_dict

def test():

    tags = count_tags('example.osm')
    pprint.pprint(tags)
    assert tags == {'bounds': 1,
                     'member': 3,
                     'nd': 4,
                     'node': 20,
                     'osm': 1,
                     'relation': 1,
                     'tag': 7,
                     'way': 1}
   

if __name__ == "__main__":
    test()


"""
Output:
{'bounds': 1,
 'member': 3,
 'nd': 4,
 'node': 20,
 'osm': 1,
 'relation': 1,
 'tag': 7,
 'way': 1}
"""
