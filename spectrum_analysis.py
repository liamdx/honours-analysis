## Dependencies
from essentia import *
from essentia.standard import *
import numpy as np


def spectrumFrames(signal, frameSize, hopSize):
    ## Required methods
    spec = Spectrum()

    ## Instantiate variables
    i , number_of_frames = 0 , 0
    frames = []
    limit = len(signal)

    ## Run through the signal and extract spectrum at provided intervals
    for i in range(limit):

        if i % 256 == 0:
            _raw_progress = i / limit
            _normalised_progress = float(_raw_progress * 100)
            print"Calculating spectral frames: total progress = %d per cent" % _normalised_progress

        if i + frameSize > limit:
            ##Fix this using FrameCutter

            number_of_frames = len(frames)
            break
        else:
            x = signal[i : i + hopSize]
            f = spec(x)
            frames.append(f)
            i = i + hopSize




    return frames


def meanSpectrum(spectrumFrames):
    # Signal must be loaded in to essentia first
    # Declaring essentia function(s)


    # Declaring Variables, container for frames
    # and length of the input signal
    j = 1
    number_of_frames = 0


    f_raw = spectrumFrames

    raw_mean_spec = f_raw[0]
    limit = len(f_raw)

    print "Calculating mean spectrum"

    for j in range(limit):
        raw_mean_spec += f_raw[j]


    normalize(raw_mean_spec)
    return  raw_mean_spec

def getSpectralPeaks(spectrumFrames):
    ## Declare functions used
    sp = SpectralPeaks()

    ## Values
    return_sp_freqs = []
    return_sp_mags = []
    i = 0
    limit = len(spectrumFrames)

    ## Get spectral peaks from
    for i in range(limit):
        x = spectrumFrames[i]
        y_freq, y_mag = sp(x)
        return_sp_freqs.append(y_freq)
        return_sp_mags.append(y_mag)

        if i % 256 == 0:
            _raw_progress = i / limit
            _normalised_progress = _raw_progress * 100
            print "Calculating spectral peaks: total progress = %d per cent" % _normalised_progress
        i += 1

    return return_sp_freqs, return_sp_mags


