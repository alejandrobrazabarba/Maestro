#!/usr/bin/python
DER = 5
IZQ = 4

import maestro as m
import time

s = m.Controller()
#The arguments of setTarget are the channel to which the servo is connected
#and the pulse width in quarters of microseconds
#So for a servo with resting position at 1500 us, you need to send 4*1500=6000
#If you send a 0 it stop sending pulses
#Because of the way the library works with binary displacements, sending -1 as
#target is equivalent to sending 16384=2^14
s.setTarget(DER,7500)
s.setTarget(IZQ,4500)

time.sleep(5)

s.setTarget(DER,0)
s.setTarget(IZQ,0)
