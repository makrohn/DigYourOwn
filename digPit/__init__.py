from artifactGen import artifactGen
import diffGen
numArts = artifactGen()
numDiff = diffGen.difficultyGen()
nameDiff = diffGen.nameDiff(numDiff)
