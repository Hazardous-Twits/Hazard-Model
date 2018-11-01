from Variables.Variable import Variable

"""
    X9i - Informational Hub Type 
"""

class X9IsInfoHub(Variable):

    def __init__(self, g):
        super().__init__("InfoHub")
        self.network = g

    def get_covariate(self, node, current_date, nonadopted):
        """
        Return 1 if node i is a official news media channel (organization), 0 otherwise

        :param node:
        :param current_date:
        :param nonadopted:
        :return: 1 if node i is a official news media channel (organization), 0 otherwise
        """
        pass