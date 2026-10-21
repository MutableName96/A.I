import cv2 as cv
import numpy as np
import os

carpeta = os.path.dirname(os.path.abspath(__file__))

dataset = (
    r"C:\Users\Tonin\OneDrive\Semestres\Semestre 9"
    r"\Alcaraz\OpenCV_Eigenfaces_Fisherfaces_LBPH\Dataset"
)

ruta_modelo = os.path.join(dataset, "laloEigenFace.xml")
ruta_etiquetas = os.path.join(dataset, "labels.npy")

ruta_frontal = os.path.join(
    carpeta, "haarcascade_frontalface_alt2.xml"
)

ruta_perfil = os.path.join(
    carpeta, "haarcascade_profileface.xml"
)

if not os.path.isfile(ruta_modelo):
    raise FileNotFoundError(
        f"No se encontro el modelo: {ruta_modelo}"
    )

if not os.path.isfile(ruta_etiquetas):
    raise FileNotFoundError(
        f"No se encontraron las etiquetas: {ruta_etiquetas}"
    )

modelo = cv.face.EigenFaceRecognizer_create()
modelo.read(ruta_modelo)

nombres = np.load(
    ruta_etiquetas, allow_pickle=True
).item()

frontal = cv.CascadeClassifier(ruta_frontal)

if frontal.empty():
    raise RuntimeError(
        "No se pudo cargar haarcascade_frontalface_alt2.xml"
    )

perfil = cv.CascadeClassifier()

if os.path.isfile(ruta_perfil):
    perfil = cv.CascadeClassifier(ruta_perfil)

camara = cv.VideoCapture(0)

if not camara.isOpened():
    raise RuntimeError("No se pudo abrir la camara.")

UMBRAL = 5000

print("Eigenfaces cargado.")
print("Personas:", list(nombres.values()))
print("Presiona ESC para salir.")

while True:
    ret, frame = camara.read()

    if not ret:
        print("No se pudo leer la camara.")
        break

    gris = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    rostros = frontal.detectMultiScale(
        gris,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(40, 40)
    )

    if len(rostros) == 0 and not perfil.empty():
        rostros = perfil.detectMultiScale(
            gris,
            scaleFactor=1.1,
            minNeighbors=4,
            minSize=(40, 40)
        )

    for (x, y, w, h) in rostros:
        rostro = gris[y:y+h, x:x+w]

        rostro = cv.resize(
            rostro,
            (100, 100),
            interpolation=cv.INTER_CUBIC
        )

        etiqueta, distancia = modelo.predict(rostro)

        if etiqueta in nombres and distancia < UMBRAL:
            nombre = nombres[etiqueta]
            color = (0, 255, 0)
            texto = f"{nombre} ({distancia:.0f})"
        else:
            color = (0, 0, 255)
            texto = f"Desconocido ({distancia:.0f})"

        cv.rectangle(
            frame, (x, y), (x+w, y+h), color, 2
        )

        cv.putText(
            frame,
            texto,
            (x, max(y-10, 20)),
            cv.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2,
            cv.LINE_AA
        )

    cv.imshow("Reconocimiento Eigenfaces", frame)

    if cv.waitKey(1) & 0xFF == 27:
        break

camara.release()
cv.destroyAllWindows()