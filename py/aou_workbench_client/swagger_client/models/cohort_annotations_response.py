# coding: utf-8

"""
    AllOfUs Client API

    The API used by AllOfUs workbench clients (including both notebooks and our UI.)

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CohortAnnotationsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'columns': 'list[str]',
        'results': 'list[object]'
    }

    attribute_map = {
        'columns': 'columns',
        'results': 'results'
    }

    def __init__(self, columns=None, results=None):
        """
        CohortAnnotationsResponse - a model defined in Swagger
        """

        self._columns = None
        self._results = None
        self.discriminator = None

        if columns is not None:
          self.columns = columns
        self.results = results

    @property
    def columns(self):
        """
        Gets the columns of this CohortAnnotationsResponse.
        An array of columns for the annotations being returned. 

        :return: The columns of this CohortAnnotationsResponse.
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """
        Sets the columns of this CohortAnnotationsResponse.
        An array of columns for the annotations being returned. 

        :param columns: The columns of this CohortAnnotationsResponse.
        :type: list[str]
        """

        self._columns = columns

    @property
    def results(self):
        """
        Gets the results of this CohortAnnotationsResponse.
        An array of JSON dictionaries, with each dictionary representing the requested annotations and/or review status for a single person. (In Java, this is represented as Map<String, Object>[]. In Python clients, this is a list[object] where each object is a dictionary. In Typescript clients, this is an Array<any> where each object is a dictionary.) Keys in the dictionaries will be \"person_id\", \"review_status\", or the name of an annotation. 

        :return: The results of this CohortAnnotationsResponse.
        :rtype: list[object]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this CohortAnnotationsResponse.
        An array of JSON dictionaries, with each dictionary representing the requested annotations and/or review status for a single person. (In Java, this is represented as Map<String, Object>[]. In Python clients, this is a list[object] where each object is a dictionary. In Typescript clients, this is an Array<any> where each object is a dictionary.) Keys in the dictionaries will be \"person_id\", \"review_status\", or the name of an annotation. 

        :param results: The results of this CohortAnnotationsResponse.
        :type: list[object]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")

        self._results = results

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CohortAnnotationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other