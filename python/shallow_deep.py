import copy

# Shallow copy :One level deep, only references of nested child objects
# DeepCopy : Full Independent Copy

org = 5
org_2 = 5
print(id(org))
print(id(org_2))

cpy = org
cpy = 6

print(id(cpy))


my_list = [0, 1, 2, 3, 4]
# Shallow copies ways to create
copy_list = copy.copy(my_list)
copy_list = my_list.copy()
copy_list = list(my_list)
copy_list = my_list[:]

org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.copy(org)
cpy[0][1] = -10  # This will also change original beacause shallow is only 1 level deep

# To make a deep copy :
cpy = copy.deepcopy(org)
