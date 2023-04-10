import pyaudio
import wave
import pynput.mouse
import numpy as np
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
THRESHOLD = 1500  

# Initializing PyAudio
p = pyaudio.PyAudio()

with p.open(format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK) as stream:

    mouse = pynput.mouse.Controller()
    noise_detected = False

    while True:
        # Reading Sound
        data = stream.read(CHUNK)
        data_int = np.frombuffer(data, dtype=np.int16)
        amplitude = np.amax(data_int)
        
        if amplitude > THRESHOLD:
            print("Sound amplitude is : ", amplitude)
            mouse.press(pynput.mouse.Button.left)
            noise_detected = True
        elif noise_detected:
            mouse.release(pynput.mouse.Button.left)
            noise_detected = False

        time.sleep(0.01)
