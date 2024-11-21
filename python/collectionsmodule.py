# collections : Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter

a = "aaaaabbccc"
my_counter = Counter(a)

print(my_counter)
print(my_counter.values())
print(my_counter.most_common())  # Using a heapq
for k, v in my_counter.items():
    print(k, v)


from collections import defaultdict

b = defaultdict()
b.popitem
