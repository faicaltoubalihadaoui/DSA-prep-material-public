########################################################################################################
# Process : Instance of the a program ( Python Interpreter, web browser)
# A process can have multiple threads inside

# Pros

# Takes advantage of multiple CPUs and cores
# Separate memory space -> Memory is not shared between processes
# Multi processing : process data on mutiple CPUs
# New process is started independently from other processes
# Processes are killable
# One GIL for each process

# Cons
# - Heavyweight
# - More memory
# - Starting a prcess is slower than starting a thread
# - Inter communication is complicated

########################################################################################################
# Thread : Entity within a process that can be scheduled ( also knows as lightweight process )
# a process can spawn multiple threads

# Pros
# All threads within a process share the same memory
# LightWeight
# Starting a thread is faster than starting a process

# Cons
# Threading is limited by GIL: Allows one thread at a time, No parralel computation for multi threading
# Not killable ( can result in memory leaks)
# Race condition ( 2 or more threads want to modify the same variable at the same time)


########################################################################################################
# GIL : Global Interpreter Lock
# A lock that allows only one thread at a time to execute in Python

# CPython: reference implementation of Python written in C
# In Cpython is not thread-safe
