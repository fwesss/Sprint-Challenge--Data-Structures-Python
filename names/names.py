# Original runtime was O(n^2) due to the nested for loops.

import time

start_time = time.time()

f = open("names_1.txt", "r")
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open("names_2.txt", "r")
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names = {name: 1 for name in names_1}

# Replace the nested for loops below with your improvements
for name in names_2:
    if name in names:
        names[name] += 1

duplicates = {name: count for (name, count) in names.items() if count > 1}

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
start_time = time.time()

faster_duplicates = set(names_1).intersection(names_2)

end_time = time.time()
print(f"{len(faster_duplicates)} duplicates:\n\n{', '.join(faster_duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
