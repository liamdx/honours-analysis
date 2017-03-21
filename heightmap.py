import essentia
from essentia.standard import *

def getFrames(audio, maxNumberOfFrames):

    ## Array to store audio frames
    frames = essentia.Pool()

    ##
    spectrum = Spectrum()

    ## Hanning windowing
    w = Windowing(type = 'hann')

    ## Calculate hopSize to avoid unneccesary frame calculations
    adjustedHopSize = len(audio) / maxNumberOfFrames

    ## Loop through the entire audio file
    for frame in FrameGenerator(audio, frameSize = 1024, hopSize = adjustedHopSize, startFromZero = True):
        spec_frame = spectrum(w(frame))
        frames.add('lowlevel.spectrums', spec_frame)

    return frames