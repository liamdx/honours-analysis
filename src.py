# Open a file dialog and extract spectral information, aggregate to file
import essentia
from essentia.standard import *
from heightmap import getFrames
from pprint import pprint
import Tkinter as tk
import tkFileDialog
import simplejson as json

## Open dialog for user to select files
root = tk.Tk()
root.withdraw()
fileNames = tkFileDialog.askopenfilenames()

loadedAudioFiles = []


for fileName in fileNames:
	loader = EqloudLoader(filename = fileName)
	loadedAudioFiles.append(loader())


dataPools = []
dataPoolsAggregated = []
specFrames = []
specFramesAggregated = []
extractor = Extractor()



for audioFile in loadedAudioFiles:
	currentExtractor = extractor(audioFile)
	currentFrames = getFrames(audioFile, 1024)
	dataPools.append(currentExtractor)
	dataPoolsAggregated.append(PoolAggregator(defaultStats = ["mean", "min", "max",])(currentExtractor))
	specFrames.append(currentFrames)
	specFramesAggregated.append(PoolAggregator(defaultStats = ["mean", "min", "max",])(currentFrames))



# Output JSON
for index, dataPool in enumerate(dataPools):
	YamlOutput(filename = fileNames[index].replace('.wav', '') + '_analysis.json', format = 'json')(dataPool)

# Output aggregated analysis JSON
for index, aggregatedPool in enumerate(dataPoolsAggregated):
	YamlOutput(filename = fileNames[index].replace('.wav', '') + '_aggregated_analysis.json', format = 'json')(aggregatedPool)

# Output heightmap JSON
for index, specFrames in enumerate(specFrames):
	YamlOutput(filename = fileNames[index].replace('.wav', '') + '_heightmap.json', format = 'json')(specFrames)

# Output aggregated heightmap JSON
for index, specFramesAggregated in enumerate(specFramesAggregated):
	YamlOutput(filename = fileNames[index].replace('.wav', '') + '_heightmap_aggregated.json', format = 'json')(specFramesAggregated)