from multiprocessing import Process
import os

processes = []
num_processes = os.cpu_count()
print(os.cpu_count())


def square_numbers():
    for i in range(100):
        i * i


# Create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

# Start
for p in processes:
    p.start()

for p in processes:
    p.join()
