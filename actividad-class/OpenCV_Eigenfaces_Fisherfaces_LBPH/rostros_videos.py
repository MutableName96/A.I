import os
import numpy as np
import cv2 as cv

# 1. Carga el archivo XML que acabamos de descargar en tu carpeta A.I
carpeta = os.path.dirname(os.path.abspath(__file__))

# 2. Cargar el clasificador XML
ruta_xml = os.path.join(
    carpeta, 'haarcascade_frontalface_alt2.xml'
)
rostro = cv.CascadeClassifier(ruta_xml)

# 2. PON AQUÍ EL NOMBRE EXACTO DE TU ARCHIVO DE VIDEO (ej. \video1.mp4)
ruta_video = r'C:\Users\Tonin\OneDrive\Semestres\Semestre 9\Alcaraz\OpenCV_Eigenfaces_Fisherfaces_LBPH\videosCaras\sleep.mp4'
cap = cv.VideoCapture(ruta_video)

# Verificar si el video realmente se pudo abrir
if not cap.isOpened():
    print(f"ERROR: No se pudo abrir el video en la ruta:\n{ruta_video}")
    print("Verifica que el nombre del archivo y la extensión (.mp4, .avi) sean correctos.")
    exit()


carpeta_salida = r'C:\Users\Tonin\OneDrive\Semestres\Semestre 9\Alcaraz\OpenCV_Eigenfaces_Fisherfaces_LBPH\Dataset\lalo'
os.makedirs(carpeta_salida, exist_ok=True)

count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Fin del video.")
        break
        
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rostros = rostro.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in rostros:
        img = frame[y:y+h, x:x+w]
        imgr = cv.resize(img, (100, 100))
        count = count + 1
        
        name = os.path.join(carpeta_salida, 'luna' + str(count) + '.jpg')
        cv.imwrite(name, imgr)
        
    cv.imshow('rostros', frame)
    
    k = cv.waitKey(1)
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
print(f"Listo. Se guardaron {count} rostros.")