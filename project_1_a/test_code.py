# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:24:25 2026

@author: krist
"""

from tools import describe_list, describe_dict


def test_describe_list():
    """Tests the total sum of a list of lists."""
    test_list = [
        [1, 2, "hello"],
        [3, 4],
        ["python", 5]
    ]

    result = describe_list(test_list)

    assert result == 15


def test_describe_dict():
    """Test the total sum of a dictionary of dictionaries."""
    test_dict = {
        "first": {
            "a": 1,
            "b": 2,
            "word": "hello"
        },
        "second": {
            "c": 3,
            "d": 4
        }
    }

    result = describe_dict(test_dict)

    assert result == 10