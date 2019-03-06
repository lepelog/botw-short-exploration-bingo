import json
import csv

goallist = [[] for i in range(25)]
with open('smallgoals.csv') as glf:
    goalreader = csv.reader(glf)
    for goal in list(goalreader)[1:]:
        # ignore empty space
        if goal[0].strip() != '':
            difficulty = int(goal[2])
            goal = {'name':goal[0], 'types':goal[1].split(',')}
            goallist[difficulty].append(goal)

# dump the json into a js function for easy import
with open('board.js','w') as bf:
    bf.write('var bingoList = ')
    json.dump(goallist, bf)
    bf.write(';')
