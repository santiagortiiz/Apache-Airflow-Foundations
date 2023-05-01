from jsonpath_ng import parse


def get_value_from_dict(data: dict, jsonpath: str):
    """
    Find the value of a key in a dictionary

    :param dict data: dictionary in which a value will be searched for using the json path
    :param str jsonpath: json path expression
    :return any: found value
    """
    expression = parse(jsonpath)
    value = [i.value for i in expression.find(data)][0]
    return value


def insert_value_in_dict(data: dict, jsonpath: str, new_value):
    """
    Insert a key-value pair in the specified json path

    :param dict data: dictionary in which a value will be inserted for using the json path
    :param str jsonpath: json path expression
    :param any new_value: value to be inserted
    """
    expression = parse(jsonpath)
    expression.update_or_create(data, new_value)
