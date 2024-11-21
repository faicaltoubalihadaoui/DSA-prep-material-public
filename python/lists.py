# Ordered, mutable, allows duplicates
lists = ["interview", "process"]

lists.insert(1, "training")
print(lists)

a = lists.pop(1)
print(lists)

lists.remove("process")  # Raise Exception when the key doesn't exist
print(lists)


lists.clear()
print(lists)

lists = ["interview", "process"]
# Ways of creating a copy of the list
list_2 = lists.copy()
# list_2 = list(lists)
# list_2 = lists[:]   Slicing creates copy

print(id(lists))
print(id(list_2))
print(lists)
print(list_2)

# Shallow vs Deep Copy ?

lists = ["interview", "process"]

print(lists.count("interview"))
print(lists.index("interview"))
