#!/usr/bin/python

import time
import maestro as m

# Crear objeto MicroMaestro
s= m.Controller()

# Asignacion de canales
sharp = 0
servo_izq = 4
servo_dcho = 5

# Distancia de evitacion (600 choque, 0 sin obstaculo)
distance= 200

# Tiempos de movimiento y pausa para estabilizacion de lectura
avance = 0.5
turning = 0.75
stopped= 0.5

# Variables y constantes para la logica de control
rotaciones = 0
NUM_ROT_MAX = 8
INICIO = 0
EVITANDO = 1
AVANZANDO = 2
estado = AVANZANDO
# Paro los motores, en el caso de que estuvieran activos
s.setTarget(servo_izq,0)
s.setTarget(servo_dcho,0)

# El comportamiento que se consigue con este script es el siguiente:
# El robot comenzara a moverse hacia adelante hasta detectar un obstaculo
# Cuando esto ocurra, se parara y comenzara a girar hasta que el sensor detecte
# un hueco libre. Si transcurren cierta cantidad de periodos de giro y aun sigue
# detectando obstaculos, el robot parara los motores hasta que el obstaculo se retire

def pararMotores():
	s.setTarget(4,0)
	s.setTarget(5,0)
	return

def girar():
	s.setTarget(4,1)
	s.setTarget(5,-1)
	return

def avanzar():
	s.setTarget(4,1)
	s.setTarget(5,1)

while True:
	pos_1 = s.getPostion(sharp)
	pos_2 = s.getPosition(sharp)
	pos = 0.5 * (pos_1 + pos_2)
	if pos > distance:
		if (estado == EVITANDO):
			if (rotaciones == NUM_ROT_MAX):
				pararMotores()
			else:
				rotaciones += 1

		else:
			pararMotores()
			time.sleep(stopped)
			girar()
			estado = EVITANDO

		time.sleep(turning)

	else:
		if (estado == EVITANDO):
			rotaciones = 0
			pararMotores()
			time.sleep(stopped)
			avanzar()
			estado = AVANZANDO
		elif (estado == INICIO):
			avanzar()
			estado = AVANZANDO

		time.sleep(avance)
			









