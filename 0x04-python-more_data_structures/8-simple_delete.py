#!/usr/bin/python3
def simple_delete(new_dict, key=""):
    if key in new_dict:
        del new_dict[key]
    return new_dict
