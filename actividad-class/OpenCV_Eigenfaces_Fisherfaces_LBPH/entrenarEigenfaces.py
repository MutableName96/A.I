import cv2 as cv
import numpy as np
import os

# Ruta del dataset
data_set = r"C:\Users\Tonin\OneDrive\Semestres\Semestre 9\Alcaraz\OpenCV_Eigenfaces_Fisherfaces_LBPH\Dataset"

if not os.path.isdir(data_set):
    raise FileNotFoundError(f"No existe el dataset: {data_set}")

personas = sorted(os.listdir(data_set))

faces_data = []
labels = []
label_names = {}

label = 0

for person in personas:
    person_path = os.path.join(data_set, person)

    if not os.path.isdir(person_path):
        continue

    cantidad = 0

    for img_name in sorted(os.listdir(person_path)):
        img_path = os.path.join(person_path, img_name)

        img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

        if img is None:
            continue

        # Eigenfaces necesita imágenes del mismo tamaño
        img = cv.resize(img, (100, 100))

        faces_data.append(img)
        labels.append(label)
        cantidad += 1

    if cantidad > 0:
        label_names[label] = person
        print(f"{person} (label={label}): {cantidad} imágenes")
        label += 1
    else:
        print(f"Aviso: no hay imágenes válidas en {person}")

if len(faces_data) == 0:
    raise ValueError("No se encontraron imágenes válidas para entrenar.")

# Entrenar Eigenfaces
face_recognizer = cv.face.EigenFaceRecognizer_create()
face_recognizer.train(faces_data, np.array(labels, dtype=np.int32))

# Guardar modelo y nombres de las etiquetas
ruta_modelo = os.path.join(data_set, "laloEigenface.xml")
face_recognizer.write(ruta_modelo)

np.save(
    os.path.join(data_set, "labels.npy"),
    label_names
)

print(f"\nEntrenamiento terminado.")
print(f"Total de imágenes: {len(faces_data)}")
print(f"Personas entrenadas: {len(label_names)}")
print(f"Modelo guardado en: {ruta_modelo}")
 