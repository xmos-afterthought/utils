import numpy as np
import struct

# From http://keystrokecountdown.com/articles/PDMPlayground/index.html

sampleFrequency = 96000 # Hz
bandwidth = sampleFrequency / 2 # 0-512 Hz (also Nyquist freq)
sampleDuration = 1.0 / sampleFrequency # time duration per cycle

signalTime = np.arange(0, 1, sampleDuration)
signal1Freq = 51 # Hz
signal1Samples = np.sin(2.0 * np.pi * signal1Freq * signalTime)
signal2Freq = 247 # Hz
signal2Samples = np.sin(2.0 * np.pi * signal2Freq * signalTime)
signalSamples = signal1Samples

pdmFreq = 32
pdmPulses = np.empty(sampleFrequency * pdmFreq)
pdmTime = np.arange(0, pdmPulses.size)

f = open("/tmp/multisine.pdm", "wb")

pdmIndex = 0
signalIndex = 0
quantizationError = 0
while pdmIndex < pdmPulses.size:
    sample = signalSamples[signalIndex]
    signalIndex += 1
    for tmp in range(pdmFreq):
        if sample >= quantizationError:
            bit = 1
        else:
            bit = -1
        quantizationError = bit - sample + quantizationError
        pdmPulses[pdmIndex] = bit
        if bit == 1:
            f.write(struct.pack('<B', 0xf))
        else:
            f.write(struct.pack('<B', 0))
        pdmIndex += 1

f.close()
