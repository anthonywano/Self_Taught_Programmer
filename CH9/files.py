import os
import csv

# os.path.join("Users", "anthonywano", "Desktop", "Lorem_ipsum.txt")
# /Users/anthonywano/Desktop/Lorem_ipsum.txt

# test = open(os.path.join("/", "Users", "anthonywano", "Desktop", "Lorem_ipsum.txt"), "w")
# test.write("Hi from Python!")
# test.close()

my_list = list()

with open(os.path.join("/", "Users", "anthonywano", "Desktop", "Lorem_ipsum.txt"), "r") as f:
    # print(f.read())
    my_list.append(f.read())

print(my_list)

with open(os.path.join("/", "Users", "anthonywano", "Desktop", "CH9_csv.csv"), "w") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(['four', 'five', 'six'])


with open(os.path.join("/", "Users", "anthonywano", "Desktop", "CH9_csv.csv"), "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
