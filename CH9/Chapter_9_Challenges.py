# 1: Find a file on your computer and print its contents

import os
import csv

with open(os.path.join("/", "Users", "anthonywano", "Documents", "School", "IST 210",
          "webspace.txt"), "r") as f:
    print(f.read())


# 2: Ask a user a question and save their answer to a file

answer = input("What is your name and age? ")

with open(os.path.join('/', 'Users', 'anthonywano', 'Desktop', 'name_age.txt'), 'w') as f:
    f.write(answer)


# 3: Write CSV with movies_list

movies_list = [["Top Gun", "Risky Business", "Minority Report"],
               ["Titanic", "The Revenant", "Inception"],
               ["Training Day", "Man on Fire", "Flight"]]

with open(os.path.join('/', 'Users', 'anthonywano', 'Desktop', 'movies_actor.csv'), 'w') as f:
    x = csv.writer(f, delimiter=',')
    for row in movies_list:
        x.writerow(row)




