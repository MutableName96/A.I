
import os
import cv2 as cv

carpeta = os.path.dirname(os.path.abspath(__file__))

# 2. Cargar el clasificador XML
ruta_xml = os.path.join(
    carpeta, 'haarcascade_frontalface_alt2.xml'
)

rostro = cv.CascadeClassifier(ruta_xml)

if rostro.empty():
    print("ERROR: No se pudo cargar el XML:", ruta_xml)
    exit()

# 3. Abrir la cámara
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: No se pudo abrir la cámara.")
    exit()

# 4. Crear carpeta de salida
# Carpeta donde se guardarán los rostros
carpeta_salida = r'C:\Users\Tonin\OneDrive\Semestres\Semestre 9\Alcaraz\OpenCV_Eigenfaces_Fisherfaces_LBPH\Dataset\Antonio'

os.makedirs(carpeta_salida, exist_ok=True)

count = 0

# 5. Capturar y guardar rostros automáticamente
while True:
    ret, frame = cap.read()

    if not ret:
        print("No se pudo capturar la imagen.")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    rostros = rostro.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in rostros:
        # Dibujar rectángulo
        cv.rectangle(
            frame, (x, y), (x+w, y+h),
            (0, 255, 0), 2
        )

        img = frame[y:y+h, x:x+w]
        imgr = cv.resize(img, (100, 100))


        count += 1
        nombre = os.path.join(
            carpeta_salida, f'garza{count}.jpg'
        )
        cv.imwrite(nombre, imgr)

    cv.putText(
        frame, f'Rostros guardados: {count}',
        (10, 30), cv.FONT_HERSHEY_SIMPLEX,
        0.7, (0, 255, 0), 2
    )

    cv.imshow('Deteccion automatica de rostros', frame)


    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()

print(f"Listo. Se guardaron {count} rostros.")
