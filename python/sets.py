# Unoderedred, mutable, no duplicates
my_set = set()

# you can't put argument for pop element for a set
my_set.add(1)
my_set.remove(1)

odds = {1, 3, 5}
evens = {0, 2, 4}

u = odds.union(evens)

i = odds.intersection(evens)

diff = odds.difference(evens)  # in odds but not in evens

setA = {1, 2, 3}
setB = {1}

setB.issubset(setA)


a = frozenset([1, 2, 3, 4])  # Immutable version of a set

# a.add(2)  # error won't work
