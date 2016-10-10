#!/usr/bin/python

import maestro as m
s = m.Controller()
#The arguments of setTarget are the channel to which the servo is connected
#and the pulse width in quarters of microseconds
#So for a servo with resting position at 1500 us, you need to send 4*1500=6000
#If you send a 0 it stop sending pulses
#Because of the way the library works with binary displacements, sending -1 as
#target is equivalent to sending 16384=2^14
s.setTarget(4,7500)
s.setTarget(5,4500)
