# coding: utf-8

"""
    WALKOFF

    An active cyber defense development framework enabling orchestration capabilities to be written once and deployed across WALKOFF-enabled orchestration tools. https://nsacyber.github.io/WALKOFF/  # noqa: E501

    The version of the OpenAPI document: 0.9.1
    Contact: walkoff@nsa.gov
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Parameter(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'walkoff_type': 'str',
        'errors': 'list[str]',
        'id_': 'str',
        'name': 'str',
        'parallelized': 'bool',
        'value': 'object',
        'variant': 'str'
    }

    attribute_map = {
        'walkoff_type': '_walkoff_type',
        'errors': 'errors',
        'id_': 'id_',
        'name': 'name',
        'parallelized': 'parallelized',
        'value': 'value',
        'variant': 'variant'
    }

    def __init__(self, walkoff_type=None, errors=None, id_=None, name=None, parallelized=False, value=None, variant=None):  # noqa: E501
        """Parameter - a model defined in OpenAPI"""  # noqa: E501

        self._walkoff_type = None
        self._errors = None
        self._id_ = None
        self._name = None
        self._parallelized = None
        self._value = None
        self._variant = None
        self.discriminator = None

        if walkoff_type is not None:
            self.walkoff_type = walkoff_type
        if errors is not None:
            self.errors = errors
        if id_ is not None:
            self.id_ = id_
        self.name = name
        if parallelized is not None:
            self.parallelized = parallelized
        if value is not None:
            self.value = value
        self.variant = variant

    @property
    def walkoff_type(self):
        """Gets the walkoff_type of this Parameter.  # noqa: E501

        Workflow type for json decoder  # noqa: E501

        :return: The walkoff_type of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._walkoff_type

    @walkoff_type.setter
    def walkoff_type(self, walkoff_type):
        """Sets the walkoff_type of this Parameter.

        Workflow type for json decoder  # noqa: E501

        :param walkoff_type: The walkoff_type of this Parameter.  # noqa: E501
        :type: str
        """

        self._walkoff_type = walkoff_type

    @property
    def errors(self):
        """Gets the errors of this Parameter.  # noqa: E501

        Errors attached to this ExecutionElement  # noqa: E501

        :return: The errors of this Parameter.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this Parameter.

        Errors attached to this ExecutionElement  # noqa: E501

        :param errors: The errors of this Parameter.  # noqa: E501
        :type: list[str]
        """

        self._errors = errors

    @property
    def id_(self):
        """Gets the id_ of this Parameter.  # noqa: E501

        A 32-bit hexadecimal string representing a globally unique identifier  # noqa: E501

        :return: The id_ of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._id_

    @id_.setter
    def id_(self, id_):
        """Sets the id_ of this Parameter.

        A 32-bit hexadecimal string representing a globally unique identifier  # noqa: E501

        :param id_: The id_ of this Parameter.  # noqa: E501
        :type: str
        """

        self._id_ = id_

    @property
    def name(self):
        """Gets the name of this Parameter.  # noqa: E501


        :return: The name of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Parameter.


        :param name: The name of this Parameter.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def parallelized(self):
        """Gets the parallelized of this Parameter.  # noqa: E501


        :return: The parallelized of this Parameter.  # noqa: E501
        :rtype: bool
        """
        return self._parallelized

    @parallelized.setter
    def parallelized(self, parallelized):
        """Sets the parallelized of this Parameter.


        :param parallelized: The parallelized of this Parameter.  # noqa: E501
        :type: bool
        """

        self._parallelized = parallelized

    @property
    def value(self):
        """Gets the value of this Parameter.  # noqa: E501

        The value of the argument OR The ID of the action whose output should be used  # noqa: E501

        :return: The value of this Parameter.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Parameter.

        The value of the argument OR The ID of the action whose output should be used  # noqa: E501

        :param value: The value of this Parameter.  # noqa: E501
        :type: object
        """

        self._value = value

    @property
    def variant(self):
        """Gets the variant of this Parameter.  # noqa: E501


        :return: The variant of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._variant

    @variant.setter
    def variant(self, variant):
        """Sets the variant of this Parameter.


        :param variant: The variant of this Parameter.  # noqa: E501
        :type: str
        """
        if variant is None:
            raise ValueError("Invalid value for `variant`, must not be `None`")  # noqa: E501
        allowed_values = ["STATIC_VALUE", "ACTION_RESULT", "WORKFLOW_VARIABLE", "GLOBAL"]  # noqa: E501
        if variant not in allowed_values:
            raise ValueError(
                "Invalid value for `variant` ({0}), must be one of {1}"  # noqa: E501
                .format(variant, allowed_values)
            )

        self._variant = variant

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Parameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
