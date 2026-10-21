import cv2 as cv
import numpy as np
import os

carpeta = os.path.dirname(os.path.abspath(__file__))

data_set = (
    r"C:\Users\Tonin\OneDrive\Semestres\Semestre 9"
    r"\Alcaraz\OpenCV_Eigenfaces_Fisherfaces_LBPH\Dataset"
)

ruta_modelo = os.path.join(
    data_set, "laloFisherFace.xml"
)

ruta_labels = os.path.join(
    data_set, "fisher_labels.npy"
)

ruta_cascade = os.path.join(
    carpeta, "haarcascade_frontalface_alt2.xml"
)

for ruta in (ruta_modelo, ruta_labels, ruta_cascade):
    if not os.path.isfile(ruta):
        raise FileNotFoundError(
            f"No se encontro el archivo:\n{ruta}"
        )

face_recognizer = cv.face.FisherFaceRecognizer_create()
face_recognizer.read(ruta_modelo)

label_names = np.load(
    ruta_labels,
    allow_pickle=True
).item()

print("Modelo Fisherfaces cargado correctamente.")
print("Personas registradas:", list(label_names.values()))

cascade = cv.CascadeClassifier(ruta_cascade)

if cascade.empty():
    raise RuntimeError(
        "No se pudo cargar haarcascade_frontalface_alt2.xml"
    )

ruta_perfil = os.path.join(
    carpeta, "haarcascade_profileface.xml"
)

cascade_perfil = cv.CascadeClassifier()

if os.path.isfile(ruta_perfil):
    cascade_perfil = cv.CascadeClassifier(ruta_perfil)

cap = cv.VideoCapture(0)

if not cap.isOpened():
    cap.release()
    raise RuntimeError("No se pudo abrir la camara.")

THRESHOLD = 300

print("Camara iniciada. Presiona ESC para salir.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("No se pudo capturar el fotograma.")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    rostros = cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(40, 40)
    )

    if len(rostros) == 0 and not cascade_perfil.empty():
        rostros = cascade_perfil.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=4,
            minSize=(40, 40)
        )

    for (x, y, w, h) in rostros:
        roi = gray[y:y+h, x:x+w]

        roi = cv.resize(
            roi,
            (100, 100),
            interpolation=cv.INTER_CUBIC
        )

        label_id, confidence = face_recognizer.predict(roi)

        if label_id in label_names and confidence < THRESHOLD:
            nombre = label_names[label_id]
            color = (0, 255, 0)
            texto = f"{nombre} ({confidence:.1f})"
        else:
            color = (0, 0, 255)
            texto = f"Desconocido ({confidence:.1f})"

        cv.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            color,
            2
        )

        cv.putText(
            frame,
            texto,
            (x, max(y - 10, 20)),
            cv.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2,
            cv.LINE_AA
        )

    cv.imshow("Reconocimiento facial - Fisherfaces", frame)

    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()

print("Camara cerrada correctamente.")