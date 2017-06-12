import sys
import wave

if len(sys.argv) != 3:
    print "Usage: pcm_to_wav.py <channel count> <input file>"
    sys.exit()

with open(sys.argv[2], 'rb') as pcmfile:
    pcmdata = pcmfile.read()

wavfile = wave.open(sys.argv[2]+'.wav', 'wb')
wavfile.setparams((int(sys.argv[1]), 4, 16000, 0, 'NONE', 'NONE'))
wavfile.writeframes(pcmdata)
wavfile.close()
