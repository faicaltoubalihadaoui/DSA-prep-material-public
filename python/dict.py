# Mutable, KV, Unordered
dict.pop("key")
del dict["key"]
dict.popitem()  # remove last element
# dicts become ordered from Python 3.7

dict.items()  # k, v
dict.values()  # v's
dict.keys()  # Keys

mydict = {}
copy_dict = dict.copy()  # For copy otherwise same element will be modified
copy_dict = dict(mydict)

old_dict = {}
newer_dict = {}

old_dict.update(newer_dict)  #

import sys

print(sys.hash_info)
