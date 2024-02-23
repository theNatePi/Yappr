import pyaudio
import wave
import sys
import numpy as num
import audioop
from math import log10


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100


def record_audio():
    print('#' * 80)
    print("Please speak word(s) into the microphone")
    print('Press Ctrl+C to stop the recording')

    record_to_file('output.wav')

    print("Result written to output.wav")
    print('#' * 80)


def record():
    p = pyaudio.PyAudio()

    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    frames = []

    sound_levels = []
    samples = 0
    for _ in range(100):
        data = stream.read(CHUNK)

        rms = audioop.rms(data, 2)
        decibel = 20 * log10(rms)

        sound_levels.append(decibel)
        samples += 1


    print("Start recording")

    timeout = 50
    was_active = False

    while True:
        data = stream.read(CHUNK)

        rms = audioop.rms(data, 2)
        decibel = 20 * log10(rms)

        sound_levels.append(decibel)
        samples += 1

        average = sum(sound_levels) / samples

        check = decibel - (abs(decibel - average) / 1.0000000000000005)

        if (check) > average:
            frames.append(data)
            timeout = 50
            was_active = True
        
        else:
            if timeout > 0 and was_active:
                frames.append(data)
                timeout -= 1
            else:
                if was_active and (len(frames) > 80):
                    break
                else:
                    frames.clear()


    sample_width = p.get_sample_size(FORMAT)

    stream.stop_stream()
    stream.close()
    p.terminate()

    return sample_width, frames


def record_to_file(file_path):
	wf = wave.open(file_path, 'wb')
	wf.setnchannels(CHANNELS)
	sample_width, frames = record()
	wf.setsampwidth(sample_width)
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()
