## Dependencies
from PIL import Image, ImageDraw
from numpy import interp

def generateHeightmapData(sizeX, sizeY, spectrumFrames, samplesPerFrame, real2smooth):
    ## Declare vars
    ## Create an image
    size = (sizeX, sizeY)
    print "Generating height-map data"

    ## Pixel limit - 1 to make working with audio easier
    ## Frames will take form 2n + 1 x 2n +1 for unity terrain error compensation
    iterator_limit = sizeX - 1
    ## How often should we plot sample value
    sample_limit = (sizeX / real2smooth) - 1

    number_of_frames = len(spectrumFrames)
    frames_required = sizeX / real2smooth
    FrameHopSize = number_of_frames / frames_required
    SampleHopSize = iterator_limit / samplesPerFrame

    ## Create array of pixel values
    final_spectrum_columns = []

    ## Maps spectrum to be suitable for pixelisation
    for k in range(frames_required):
        spectrum_column = []
        currentFrame = spectrumFrames[k * FrameHopSize]

        for t in range(sample_limit):
            currentValue = currentFrame[t]
            spectrum_column.append(currentValue)

        final_spectrum_columns.append(spectrum_column)

    xx = final_spectrum_columns[0]
    print xx
    print xx[0]

    return final_spectrum_columns
