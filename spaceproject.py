from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

b = (0, 0, 0)          # black
l = (145, 145, 145)    # light gray
e = (28, 74, 142)      # blue
m = (97, 97, 97)       # middle gray
d = (78, 78, 78)       # dark grey
g = (0, 255, 0)        # green

image1 = [b,b,b,m,e,e,m,e,
        e,e,e,m,l,l,l,e,
        e,e,e,m,b,l,b,e,
        g,e,e,m,l,l,l,e,
        e,l,l,l,l,l,l,e,
        e,l,l,l,e,l,e,e,
        e,l,e,l,e,l,l,e,
        e,d,e,d,e,e,e,e
]


for i in range(10):
    sense.set_pixels(image1)
    sleep(1)
























