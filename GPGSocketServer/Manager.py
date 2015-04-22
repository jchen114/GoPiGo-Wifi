__author__ = 'Kingpin'

from gopigo import *
import sys

import atexit
atexit.register(stop)

class GPGManager:

    def __init__(self):
        # stuff
	print 'initialize GPGManager'

    def go_forward(self):
        fwd()

    def go_backward(self):
        bwd()

    def turn_left(self):
        left()

    def turn_right(self):
        right()

    def stop(self):
        stop()

