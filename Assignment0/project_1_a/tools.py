# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:24:25 2026

@author: krist
"""
def describe_list(nested_list):
    """


    Args:
        nested_list (list): A list containing other lists.

    Returns:
         - the total number of inner lists,
        - the contents of each inner list,
        - the sum of numerical values in each inner list,
        - the total sum of all numerical values.
    """
    total_sum = 0

    print(f"Number of lists: {len(nested_list)}")

    for index, inner_list in enumerate(nested_list, start=1):
        list_sum = 0

        for item in inner_list:
            if isinstance(item, (int, float)):
                list_sum += item

        print(f"List {index} contains elements: {inner_list}")
        print(f"Numeric sum of list {index}: {list_sum}")

        total_sum += list_sum

    print(f"Total sum of all numerical values: {total_sum}")

    return total_sum

def describe_dict(nested_dict):
    """
       Args:
        nested_dict (dict): A dictionary containing other dictionaries.

    Returns:
         - the total number of inner dictionaries,
        - the contents of each inner dictionary,
        - the sum of numerical values in each inner dictionary,
        - the total sum of all numerical values.
    """
    total_sum = 0

    print(f"Number of dictionaries: {len(nested_dict)}")

    for name, inner_dict in nested_dict.items():
        dict_sum = 0

        for value in inner_dict.values():
            if isinstance(value, (int, float)):
                dict_sum += value

        print(f"Dictionary '{name}' contains: {inner_dict}")
        print(f"Numeric sum of dictionary '{name}': {dict_sum}")

        total_sum += dict_sum

    print(f"Total sum of all numerical values: {total_sum}")

    return total_sum