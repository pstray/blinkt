#!/usr/bin/env python

from blinkt import set_brightness, set_pixel, show
import time
import math
import colorsys

hue_range = 120
hue_start = 0
max_brightness = 0.2

def show_graph(v, r, g, b):
    v *= 8
    for x in range(8):
        hue = ((hue_start + ((x/8.0) * hue_range)) % 360) / 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue,1.0,1.0)]
        if v  < 0:
            brightness = 0
        else:
            brightness = min(v,1.0) * max_brightness
        set_pixel(x, r, g, b, brightness)
        v -= 1

    show()

set_brightness(0.1)

try:
    while True:
        t = time.time() * 2
        v = (math.sin(t) + 1) / 2 # Get a value between 0 and 1
        show_graph(v,255,0,255)
        time.sleep(0.01)

except KeyboardInterrupt:
    pass
