import matplotlib.pyplot as plot
import numpy
import numpy.fft as fft
import subprocess as sp

FFMPEG_BIN = "ffmpeg"
command = [FFMPEG_BIN,
           '-i', 'data/origin/1.mp3',
           '-f', 's16le',
           '-acodec', 'pcm_s16le',
           '-ar', '44100',  # ouput will have 44100 Hz
           '-ac', '2',  # stereo (set to '1' for mono)
           '-']
pipe = sp.Popen(command, stdout=sp.PIPE, bufsize=10 ** 8)

raw_audio = pipe.stdout.read(88200 * 10)
audio_array = numpy.fromstring(raw_audio, dtype="int16")
audio_array = audio_array[::2]
arrs = numpy.array_split(audio_array, 1)

for subarr in arrs:
    fft_sign = numpy.abs(fft.rfft(subarr))
    plot.plot(fft_sign)
    plot.show()
# Reorganize raw_audio as a Numpy array with two-columns (1 per channel)

# plot.plot(audio_array)
