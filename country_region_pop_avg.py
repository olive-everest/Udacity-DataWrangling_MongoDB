#!/usr/bin/env python
"""
Use an aggregation query to answer the following question. 

Extrapolating from an earlier exercise in this lesson, find the average regional city population 
for all countries in the cities collection. What we are asking here is that you first calculate the 
average city population for each region in a country and then calculate the average of all the 
regional averages for a country. As a hint, _id fields in group stages need not be single values. 
They can also be compound keys (documents composed of multiple fields). You will use the same 
aggregation operator in more than one stage in writing this aggregation query. I encourage you to 
write it one stage at a time and test after writing each stage.

Please modify only the 'make_pipeline' function so that it creates and returns an aggregation 
pipeline that can be passed to the MongoDB aggregate function. As in our examples in this lesson, 
the aggregation pipeline should be a list of one or more dictionary objects. 
Please review the lesson examples if you are unsure of the syntax.

"""

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    pipeline = [ {'$match' : {'country' : {'$exists' : 1},
                              'name' : {'$exists' : 1} } },
                 {'$unwind' : '$isPartOf'},
                 {'$group' : {'_id' : {'country' : '$country', 
                                       'region' : '$isPartOf'}, 
                            'region_pop_avg' : {'$avg' : '$population'} } },
                 {'$group' : {'_id' : '$_id.country',
                              'avgRegionalPopulation' : {'$avg' : '$region_pop_avg'} } },
                 {'$sort' : {'avgRegionalPopulation' : -1} }
                ]
    return pipeline

def aggregate(db, pipeline):
    result = db.cities.aggregate(pipeline)
    return result

if __name__ == '__main__':
    # The following statements will be used to test your code by the grader.
    # Any modifications to the code past this point will not be reflected by
    # the Test Run.
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    if len(result["result"]) < 150:
        pprint.pprint(result["result"])
    else:
        pprint.pprint(result["result"][:100])
    for country in result["result"]:
        if country["_id"] == 'Algeria':
            assert country["_id"] == 'Algeria'
            assert country["avgRegionalPopulation"] == 187590.19047619047
    assert {'_id': 'Algeria', 
            'avgRegionalPopulation': 187590.19047619047} in result["result"]


"""
Result:
[{u'_id': u'The_Democratic_Republic_Of_Congo',
  u'avgRegionalPopulation': 9046000.0},
 {u'_id': u'Saudi Arabia', u'avgRegionalPopulation': 1826254.75},
 {u'_id': u'Cuba', u'avgRegionalPopulation': 1701228.0},
 {u'_id': u'Kenya', u'avgRegionalPopulation': 1226727.4285714286},
 {u'_id': u'Ghana', u'avgRegionalPopulation': 1185798.5},
 {u'_id': u'Tunisia', u'avgRegionalPopulation': 1138517.5},
 {u'_id': u'Honduras', u'avgRegionalPopulation': 1126534.0},
 {u'_id': u'Zambia', u'avgRegionalPopulation': 1103957.4285714286},
 ...]
"""
