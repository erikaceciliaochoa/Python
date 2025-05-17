import cv2
from cvzone.HandTrackingModule import HandDetector

# Inicializa la cámara web
webcam = cv2.VideoCapture(0) # 1

# Inicializa el rastreador de manos
rastreador = HandDetector(detectionCon=0.8, maxHands=2)

while True:
	# Captura la imagen en el cuadro
	exito, imagen = webcam.read()
	coordenadas, imagen_manos = rastreador.findHands(imagen)
	
	print(coordenadas)

    # Muestra el cuadro con las marcas
	cv2.imshow("Proyecto 4 - IA", imagen)
	
    # Cierra la aplicación cuando se presiona cualquier tecla
	if cv2.waitKey(1) != -1:
		break
	
webcam.release() # liberamos la camara
cv2.destroyAllWindows() # cierra las ventanas

# Ctrl+Shift+P  -> seleccionar interprete version 3.12.7