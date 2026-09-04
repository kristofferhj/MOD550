# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:20:21 2026

@author: krist
"""
from tools import describe_list, describe_dict


my_lists = [
    [1, 3, "mn"],
    [5, "apple", 2.5],
    ["hello", 4]
]

my_dicts = {
    "fridge": {
        "temperature": 4,
        "milk": 2,
        "eggs": 6
    },
    "freezer": {
        "temperature": -18,
        "pizza": 3,
        "ice_cream": 2
    }
}


print("LIST INFO")
describe_list(my_lists)

print()

print("DICTIONARY INFO")
describe_dict(my_dicts)