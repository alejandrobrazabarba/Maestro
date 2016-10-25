#!/usr/bin/python

# La principal diferencia de este script con respecto al anterior 3avoid_obstacles.py , 
# es que una vez que el robot ha detectado un obstaculo y comienza a girar, 
# la comprobacion de la distancia al obstaculo se realiza sin necesidad de que 
# el robot pare para luego arrancar. El robot solo dejara de girar si encuentra 
# un hueco libre, o si pasa mucho tiempo girando.

import time
import maestro as m

# Crear objeto MicroMaestro
s= m.Controller()

# Asignacion de canales
sharp = 0
servo_izq = 4
servo_dcho = 5

#Distancia de evitacion (600 choque, 0 sin obstaculo)
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

### FUNCIONES ###
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
	return
#################

### BUCLE PRINCIPAL ###
while True:
	pos_1 = s.getPosition(sharp)
	pos_2 = s.getPosition(sharp)
	pos = 0.5 * (pos_1 + pos_2)
	if pos > distance:
		# Se detecta un obstaculo
		if (estado == EVITANDO):
			# Ya estabamos evitando el obstaculo
			if (rotaciones == NUM_ROT_MAX):
				# Hemos alcanzado el limite de rotaciones
				pararMotores()
			else:
				# Continuamos girando
				rotaciones += 1

		else:
			# Llegamos aqui en el caso de que
			# estado valga INICIO o AVANZANDO
			pararMotores()
			time.sleep(stopped)
			girar() # Comenzamos a girar
			estado = EVITANDO # Recordamos que hemos empezado a girar

		# Esperamos antes de continuar
		time.sleep(turning)

	else:
		# No detectamos un obstaculo cerca
		if (estado == EVITANDO):
			# Si previamente estabamos evitando un obstaculo
			rotaciones = 0 # reseteamos contador
			pararMotores() # nos paramos
			time.sleep(stopped) # evitamos picos de corriente en el motor
			avanzar() # comenzamos a avanzar
			estado = AVANZANDO # recordamos que avanzamos
		elif (estado == INICIO):
			# Si estamos en la fase de inicio del programa 
			avanzar() # comenzamos a avanzar
			estado = AVANZANDO # recordamos que avanzamos
		#elif (estado == AVANZANDO):
			# Aqui no hacemos nada, por eso no es necesario contemplarlo

		# Esperamos antes de continuar
		time.sleep(avance)
			
#######################








