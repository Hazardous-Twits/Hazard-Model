from Variables.Variable import Variable
from pymongo import MongoClient

import argparse
from Utils.NetworkUtils import *

"""
    X9i - Informational Hub Type 
"""

class X9IsInfoHub(Variable):

    def __init__(self, g):
        super().__init__("InfoHub")
        self.network = g

    def get_covariate(self, node, current_date, nonadopted):
        """
        Return 1 if node i is an official news media channel (organization), 0 otherwise
        Checks if the user is:
        - verified
        - has "news" in description or name

        :param node:
        :param current_date:
        :param nonadopted:
        :return: 1 if node i is a official news media channel (organization), 0 otherwise
        """
        database = MongoClient()['stream_store']
        query_string = {"user.id_str": node}
        tweet = database.tweets.find_one(query_string)

        assert(tweet != None)

        description = str(tweet["user"]["description"])
        name = tweet["user"]["name"]

        return tweet["user"]["verified"] and ("news" in description.lower() or "news" in name.lower())

if __name__ == "__main__":
    program_description = "IsInfoHub"
    parser = argparse.ArgumentParser(description=program_description)
    parser.add_argument('g', help='Input network graph')

    arguments=vars(parser.parse_args())
    g = get_graphml(arguments['g'])
    var = X9IsInfoHub(g)
    for n in var.network.nodes():
        print(var.get_covariate(n,None,None))
