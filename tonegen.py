from math import sin, pi
import numpy as np
class ToneGen():
    
    def __init__(self, pygame, freq_l, freq_r, duration=1):

        n_samples = int(round(duration*44100))
        #setup our numpy array to handle 16 bit ints, which is what we set our mixer to expect with "bits" up above
        buf = np.zeros((n_samples, 2), dtype = np.int16)
        max_sample = 2**(16 - 1) - 1

        for s in range(n_samples):
            t = float(s)/44100    # time in seconds

            #grab the x-coordinate of the sine wave at a given time, while constraining the sample to what our mixer is set to with "bits"
            buf[s][0] = int(round(max_sample*sin(2*pi*freq_l*t)))        # left
            buf[s][1] = int(round(max_sample*0.5*sin(2*pi*freq_r*t)))    # right
        pygame.sndarray.make_sound(buf).play()
        