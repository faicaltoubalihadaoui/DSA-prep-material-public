# Ordered, immutable, text representation

# Random Access
# Slicing

# Concatenation =>  str_1 + str_2
from timeit import default_timer

my_string = "      Hello World    "
my_string = my_string.strip()
print(my_string)

my_string.upper()
my_string.lower()
my_string.startswith("Hello")
my_string.endswith("World")
my_string.find("lo")  # return the index of the first occurence
my_string.count("o")
my_string.replace("World", "Universe")

my_list = my_string.split()
print(my_list)

start = default_timer()
new_string = "".join(my_list)  # from list to str
end = default_timer()
print(end - start)


# bad way of doing it
my_string = ""
for i in my_list:
    my_string += i
# time consuming

var = 3.12
var_2 = 7
my_string = f"the variable is {var} and {var_2}"
