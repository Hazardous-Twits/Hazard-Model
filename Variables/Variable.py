# TODO For Swati, followed by X4Sentiment example, inherit this class and overwrite the get_covariates function
from abc import ABC, abstractmethod


class Variable(ABC):
    def __init__(self, name):
        """
        Initilize varialbe
        :param name:            Variable name 
        """
        self.name = name

    @abstractmethod
    def get_covariate(self, node, current_date, nonadopted_nodes):
        """
        :param node:                Current node
        :param current_date:        Current date
        :param nonadopted_nodes:    Current non-adopters at this step, this object is immutable for safety concern
        :return:
        """
        pass
