import matplotlib.pyplot as plot
import numpy
import numpy.fft as fft
import subprocess as sp

arr = numpy.arange(1, 1000, 1)
sign = numpy.sin(arr * 1)
fft_sign = numpy.abs(fft.hfft(sign))
plot.plot(fft_sign)
plot.show()

FFMPEG_BIN = "ffmpeg"
command = [FFMPEG_BIN,
           '-i', '/Users/pavel/Music/muse_-_supermassive_black_hole.mp3',
           '-f', 's16le',
           '-acodec', 'pcm_s16le',
           '-ar', '44100',  # ouput will have 44100 Hz
           '-ac', '2',  # stereo (set to '1' for mono)
           '-']
pipe = sp.Popen(command, stdout=sp.PIPE, bufsize=10 ** 8)

raw_audio = pipe.stdout.read(88200 * 10)
audio_array = numpy.fromstring(raw_audio, dtype="int16")
arrs = numpy.array_split(audio_array, 10)

for subarr in arrs:
    fft_sign = numpy.abs(fft.rfft(subarr))
    plot.plot(fft_sign)
    plot.show()

# Reorganize raw_audio as a Numpy array with two-columns (1 per channel)

# audio_array = audio_array.reshape((len(audio_array)/2,2))

# plot.plot(audio_array)
