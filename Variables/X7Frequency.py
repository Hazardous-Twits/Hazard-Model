from Variables.Variable import Variable
import json
import math

"""
    X7i - Logarithm of node i’s historical tweeting frequencies on Twitter
"""


class X7Frequency(Variable):
    def __init__(self, g, historical_data):
        '''
        :param file_name: file containing historical tweets in json format
        '''
        super().__init__("HistoricalTweetingFrequency")
        self.network = g
        self.historical_tweets = json.load(open(historical_data, 'r'))

    def get_covariate(self, node, current_date, nonadopted):
        """
        :param node:
        :param current_date:
        :param nonadopted:
        :return: log of node's historical tweeting frequency
        """
        count = 0
        for tweet in self.historical_tweets:
            # referred to old_tweets_2017's format in stream_store
            if (tweet['user_id'] == node):
                count += 1
        return math.log(count)
