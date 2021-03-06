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


class TableQuery(object):
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
        'table_name': 'str',
        'columns': 'list[str]',
        'filters': 'ResultFilters',
        'concept_set_name': 'str',
        'order_by': 'list[str]'
    }

    attribute_map = {
        'table_name': 'tableName',
        'columns': 'columns',
        'filters': 'filters',
        'concept_set_name': 'conceptSetName',
        'order_by': 'orderBy'
    }

    def __init__(self, table=None, table_name=None, columns=None, filters=None, concept_set_name=None, order_by=None):
        """
        TableQuery - a model defined in Swagger
        """

        self._table_name = None
        self._columns = None
        self._filters = None
        self._concept_set_name = None
        self._order_by = None
        self.discriminator = None

        self.table_name = table.table_name if table else table_name
        if columns is not None:
          self.columns = columns
        if filters is not None:
          self.filters = filters
        if concept_set_name is not None:
          self.concept_set_name = concept_set_name
        if order_by is not None:
          self.order_by = order_by

    @property
    def table_name(self):
        """
        Gets the table_name of this TableQuery.
        The name of a table containing a person_id column to retrieve data from (e.g. person, observation); should be in the OMOP CDM 5.2 schema. 

        :return: The table_name of this TableQuery.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """
        Sets the table_name of this TableQuery.
        The name of a table containing a person_id column to retrieve data from (e.g. person, observation); should be in the OMOP CDM 5.2 schema. 

        :param table_name: The table_name of this TableQuery.
        :type: str
        """
        if table_name is None:
            raise ValueError("Invalid value for `table_name`, must not be `None`")

        self._table_name = table_name

    @property
    def columns(self):
        """
        Gets the columns of this TableQuery.
        An array of columns to retrieve from the table, taken from the table specified above. Defaults to all columns. 

        :return: The columns of this TableQuery.
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """
        Sets the columns of this TableQuery.
        An array of columns to retrieve from the table, taken from the table specified above. Defaults to all columns. 

        :param columns: The columns of this TableQuery.
        :type: list[str]
        """

        self._columns = columns

    @property
    def filters(self):
        """
        Gets the filters of this TableQuery.
        Filters on the results. Only results matching the criteria specified in the filters will be returned. If both filters and conceptSetName are specified, results must match both. 

        :return: The filters of this TableQuery.
        :rtype: ResultFilters
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """
        Sets the filters of this TableQuery.
        Filters on the results. Only results matching the criteria specified in the filters will be returned. If both filters and conceptSetName are specified, results must match both. 

        :param filters: The filters of this TableQuery.
        :type: ResultFilters
        """

        self._filters = filters

    @property
    def concept_set_name(self):
        """
        Gets the concept_set_name of this TableQuery.
        A name of a concept set in the workspace used to filter results; results must match one of the concepts in the named concept set. If both filters and conceptSetName are specified, results must match both. 

        :return: The concept_set_name of this TableQuery.
        :rtype: str
        """
        return self._concept_set_name

    @concept_set_name.setter
    def concept_set_name(self, concept_set_name):
        """
        Sets the concept_set_name of this TableQuery.
        A name of a concept set in the workspace used to filter results; results must match one of the concepts in the named concept set. If both filters and conceptSetName are specified, results must match both. 

        :param concept_set_name: The concept_set_name of this TableQuery.
        :type: str
        """

        self._concept_set_name = concept_set_name

    @property
    def order_by(self):
        """
        Gets the order_by of this TableQuery.
        An array of columns to sort the resulting data by, taken from the table specified above, each one optionally enclosed in \"DESCENDING()\" for descending sort order. Default sort order is \"person_id\" (in ascending order) followed by the ID of the specified table (in ascending order.) 

        :return: The order_by of this TableQuery.
        :rtype: list[str]
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """
        Sets the order_by of this TableQuery.
        An array of columns to sort the resulting data by, taken from the table specified above, each one optionally enclosed in \"DESCENDING()\" for descending sort order. Default sort order is \"person_id\" (in ascending order) followed by the ID of the specified table (in ascending order.) 

        :param order_by: The order_by of this TableQuery.
        :type: list[str]
        """

        self._order_by = order_by

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
        if not isinstance(other, TableQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
