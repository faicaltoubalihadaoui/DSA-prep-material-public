# Ordered, immutable, allows duplicates
tuple_obj = ("Interview", 10)
tuple_obj = ("Interview",)  # 1 element tuple

tuple_obj = tuple(["Interview", 10])

item = tuple_obj[0]
# Random Access like lists

if "Interview" in tuple_obj:
    print("True")

my_tuple = ("a", "p", "p", "l", "e")
my_tuple.count("p")
my_tuple.index("p")

my_tuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple
# i2 = [1,2,3]
import sys

print(sys.getsizeof(my_tuple))  # The size in Bytes
# Creating a list takes more time than creating a tuple
