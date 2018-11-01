from Variables.Variable import Variable

"""
    X10i:q - 1 if node i is a social hub (influential), 0 otherwise
            Define hubs as people with both in- and out-degrees
            that are larger than three standard deviations above the
            mean (Goldenberg et al. 2009)
"""

class X10IsSocialHub(Variable):

    def __init__(self, g):
        super().__init__("SocialHub")
        self.network = g

    def get_covariate(self, node, current_date, nonadopted):
        """
        Return 1 if node's in- and out-degrees
        are both three standard deviations above
        the mean, 0 otherwise


        :param node:
        :param current_date:
        :param nonadopted:
        :return: 1 if node is a social hub, 0 otherwise
        """
        pass