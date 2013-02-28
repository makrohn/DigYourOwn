import random
difficulty = {1: 'clay', 2: 'rocky till', 3: 'roots', 4: "silt", 5: "beach sand"}
def difficultyGen():
    numDiff = random.randint(1,5)
    return numDiff
def nameDiff(numDiff):
    nameDiff = difficulty[numDiff]
    return nameDiff
