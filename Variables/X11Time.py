from Variables.Variable import Variable

"""
    X11(1), X11(2), ..., X11(T) - Time dummies for each period
"""

class X11Time(Variable):

    def __init__(self, g, step):
        super().__init__("Period" + str(step))
        self.network = g
        self.period = step

    def get_covariate(self, node, current_date, nonadopted):
        """
        Return 1 if current date is in this period (0, 1, ..., T), 0 otherwise

        :param node:
        :param current_date:
        :param nonadopted:
        :return: 1 for this period, 0 otherwise
        """

        #TODO might need revision, node's adoption date or current_date?
        #TODO dummy for each period or less 1? starting period 0 or 1?
        return int(current_date == self.network.startdate + self.period * self.network.interval)
