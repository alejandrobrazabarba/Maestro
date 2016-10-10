#!/usr/bin/python

import maestro as m
s = m.Controller()

#This is equivalent to send a 6000 as target
#but this method is more efficient as it makes the micro maestro stops
#sending pulses to the servo
s.setTarget(4,0)
s.setTarget(5,0)
