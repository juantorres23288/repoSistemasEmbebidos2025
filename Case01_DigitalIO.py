import RPi.GPIO as GPIO #llamar a la libreria que permite utilizar los pines GPIO y renombrarla de una manera mas accesible 
import time # llamar a la libreria que permite trabajar con funciones de manejo

PIN_BOTON = 3 
PIN_LED = 7

estadoBoton = 0 #inicializar una variable para almacenar el estado del boton 

GPIO.setmode(GPIO.BOARD) #.BOARD significa que será físico #configurar los pines de Raspberry según la numeración fisica
GPIO.setup(PIN_LED, GPIO.OUT) # configurar el PIN FISICO 7 como una salida 
GPIO.setup(PIN_BOTON, GPIO.IN)

while true: #ciclo infinito (void loop)
	estadoBoton = GPIO.input(PIN_BOTON) #leer entrada digital
	GPIO.output(7, estadoBoton) #enviar el estado del botón al pin 7 (digitalWrite)

	if estadoBoton == 1:
		print("ENCENDIDO") # si el botón esta presionado imprima mensaje de encendido 
		time.sleep(1) # realizar pausa de un segundo
	else:
		print("APAGADO") # si el botón no esta presionado dara msn de apagado
		time.sleep(1)
