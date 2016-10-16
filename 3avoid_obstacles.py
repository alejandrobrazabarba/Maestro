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

# Paro los motores, en el caso de que estuvieran activos
s.setTarget(servo_izq,0)
s.setTarget(servo_dcho,0)

# El comportamiento que se consigue con este script es el siguiente:
# El robot comenzara a moverse hacia adelante indefinidamente en el caso de que no perciba ningun obstaculo
# Una vez que lo detecte, parara los motores durante un instante, para posteriormente girar sobre sí mismo
# para asi evitar el obstaculo. Tras este giro, que durara el tiempo especificado por la variable turning, el robot
# volvera a pararse y volvera a comprobar si hay un obstaculo. Si se produce un numero de giros superior a un maximo,
# el robot permanecera parado, en espera de que el obstaculo desaparezca, comprobando periodicamente la distancia a este.

# Lecturas de distancia a obstaculo antes de arrancar
iter=1
while (1):
	pos_min = s.getPosition(sharp)
	pos_max = s.getPosition(sharp)
	pos=0.5*(pos_min+pos_max)
	print "ITERACION ",iter
	iter = iter+1
	print "Distancia (600-0)=",pos
	if pos > distance:
		print "Me paro pq hay obstaculo"
                s.setTarget(4,0)
                s.setTarget(5,0)
                time.sleep(stopped)
		if (rotaciones < NUM_ROT_MAX):
			print "Rotando para evitar obstaculo"
			s.setTarget(4,1)
			s.setTarget(5,-1)
			rotaciones += 1
	        	time.sleep(turning)
	                s.setTarget(4,0)
	                s.setTarget(5,0)
			time.sleep(stopped)
		else:
			time.sleep(2*stopped)

	else:
		rotaciones = 0
		s.setTarget(4,1)
		s.setTarget(5,1)
		time.sleep(avance)




