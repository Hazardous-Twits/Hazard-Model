from Variables.Variable import Variable

"""
    X8i - Node i’s strength of interest in the topic of entertainment on a 0-1 scale 
          (based on topic modeling results)
"""


class X8Interest(Variable):
    def __init__(self, g):
        super().__init__("IntrinsicInterest")
        self.network = g

    def get_covariate(self, node, current_date, nonadopted):
        """
        :param node:
        :param current_date:
        :param nonadopted:
        :return: node's interest in topic on a 0-1 scale
        """
        pass