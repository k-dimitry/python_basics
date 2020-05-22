import os

line_counter = 0

for directory in os.walk("../Basics_of_Python_Programming"):
    if "week" in directory[0]:
        for filename in directory[2]:
            if filename.endswith(".py"):
                with open(directory[0] + os.sep + filename) as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            line_counter += 1

print(line_counter)  # 1580
