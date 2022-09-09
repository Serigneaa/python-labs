# Write a code snippet that gives a name to a `sheep`
# and uses a boolean value to define whether it has `wool` or not.
merino_rambouillet = "sheep with wool, originate at rambouillet"
merino_arles = "sheep with wool, originate at arles"
merino_east = "sheep with wool, originate at east"
charmoise = "meat breeds sheep"
lacaune = "dairy breed sheep"

result_1 = 'wool' in merino_rambouillet #True
if result_1 is True:
    print(merino_rambouillet, "has wool")

else:
    print(merino_rambouillet, "has not wool")

result_2 = 'wool' in merino_arles #True
if result_2 is True:
    print(merino_arles, "has wool")

else:
    print(merino_arles, "has not wool")

