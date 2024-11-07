import cv2
import numpy as np

def get_limits(color):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit

# Inicia a captura de vídeo
cap = cv2.VideoCapture(0)

while True:
    # Captura frame a frame
    ret, frame = cap.read()
    if not ret:
        break

    # Converte a imagem BGR para o espaço de cores HSV
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definindo a cor amarela em BGR
    yellow = [0, 255, 255] # Amarelo em BGR
    lowerLimit, upperLimit = get_limits(color=yellow)

    # Definindo a cor verde em BGR
    #green = [0, 255, 0] # Verde em BGR
    #lowerLimit, upperLimit = get_limits(color=green)

    # Definindo a cor azul em BGR
    #blue = [255, 0, 0] # Azul em BGR
    #lowerLimit, upperLimit = get_limits(color=blue)

    # Definindo a cor ciano em BGR
    #cian = [255, 255, 0] # Ciano em BGR
    #lowerLimit, upperLimit = get_limits(color=cian)

    # Definindo a cor roxo em BGR
    #purple = [255, 0, 255] # Roxo em BGR
    #lowerLimit, upperLimit = get_limits(color=purple)

    # Definindo a cor laranja em BGR
    #orange = [0, 125, 255] # laranja em BGR
    #lowerLimit, upperLimit = get_limits(color=orange)

    # Cria uma máscara para a cor
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # Encontra contornos na máscara
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Desenha retângulos em volta dos contornos encontrados
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostra o frame resultante
    cv2.imshow('frame', frame)

    # Sai do loop ao pressionar a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a captura e fecha as janelas
cap.release()
cv2.destroyAllWindows()