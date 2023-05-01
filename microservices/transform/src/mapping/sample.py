from src.utils import dict_ops

def map_schema(source_data, schema):
    """
    Map values from one dictionary to another, based on a schema

    Example:
        args:
            source_data = {
                "some_field": "some_value"
            }
            some_schema = {
                "some_field": "target_field"
            }
        output:
            transformed_data = {
                "target_field": "some_value"
            }
    """
    transformed_data = {}

    for source_field, target_field in schema.items():
        # Find the value of a field in the source data
        source_value = dict_ops.get_value_from_dict(source_data, source_field)

        # Assigns the found value to the target field
        dict_ops.insert_value_in_dict(transformed_data, target_field, source_value)

    return transformed_data