import matplotlib.pyplot as plot
import numpy
import numpy.fft as fft
import subprocess as sp


def crosscorr(sample, base):
    fft_1 = fft.rfft(sample)
    fft_2 = numpy.conj(fft.rfft(base))
    cross_corr = fft.irfft(fft_1 * fft_2)
    return cross_corr


dFreq = 8000
dsFactor = 1
chunkDuration = 1

FFMPEG_BIN = "ffmpeg"
command = [FFMPEG_BIN,
           '-i', 'data/origin/1.mp3',
           '-f', 's16le',
           '-acodec', 'pcm_s16le',
           '-ar', str(dFreq),  # ouput will have 44100 Hz
           '-ac', '1',  # stereo (set to '1' for mono)
           '-']
pipe = sp.Popen(command, stdout=sp.PIPE, bufsize=10 ** 8)

raw_audio = pipe.stdout.read()
audio_array = numpy.fromstring(raw_audio, dtype="int16")

audio_array = audio_array[::dsFactor]

len = audio_array.size / (chunkDuration * dFreq / dsFactor)
arrs = numpy.array_split(audio_array, len)

delay = 3
sample = audio_array[(dFreq*delay):((dFreq*delay) + arrs[0].size)]

for subarr in arrs:
    cc = crosscorr(sample, subarr)
    plot.plot(numpy.abs(cc))
    plot.show()
# Reorganize raw_audio as a Numpy array with two-columns (1 per channel)

# plot.plot(audio_array)
