import cv2 as cv
import numpy as np
import os

# Ruta del dataset
data_set = r"C:\Users\Tonin\OneDrive\Semestres\Semestre 9\Alcaraz\OpenCV_Eigenfaces_Fisherfaces_LBPH\Dataset"

if not os.path.isdir(data_set):
    raise FileNotFoundError(f"No existe el dataset: {data_set}")

# Obtener carpetas de personas
personas = sorted(
    d for d in os.listdir(data_set)
    if os.path.isdir(os.path.join(data_set, d))
)

print("Personas encontradas:", personas)

faces_data = []
labels = []
label_names = {}

label = 0

for person in personas:
    person_path = os.path.join(data_set, person)

    # Leer todas las imágenes compatibles
    archivos = sorted(
        f for f in os.listdir(person_path)
        if f.lower().endswith(
            (".jpg", ".jpeg", ".png", ".bmp")
        )
    )

    cantidad = 0

    for img_name in archivos:
        img_path = os.path.join(person_path, img_name)

        img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

        if img is None:
            print(f"No se pudo leer: {img_path}")
            continue

        # Normalizar el tamaño
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

# Fisherfaces necesita al menos dos personas
if len(label_names) < 2:
    raise ValueError(
        "Se necesitan imágenes válidas de al menos dos personas."
    )

print(f"\nTotal de imágenes: {len(faces_data)}")
print(f"Total de personas: {len(label_names)}")
print("Iniciando entrenamiento Fisherfaces...")

# Entrenar
face_recognizer = cv.face.FisherFaceRecognizer_create()

face_recognizer.train(
    faces_data,
    np.array(labels, dtype=np.int32)
)

# Guardar modelo
ruta_modelo = os.path.join(data_set, "laloFisherFace.xml")
face_recognizer.write(ruta_modelo)

# Guardar correspondencia entre etiquetas y nombres
ruta_labels = os.path.join(data_set, "fisher_labels.npy")
np.save(ruta_labels, label_names)

print("\nEntrenamiento terminado.")
print(f"Imágenes utilizadas: {len(faces_data)}")
print(f"Personas entrenadas: {len(label_names)}")
print(f"Modelo guardado: {ruta_modelo}")
print(f"Etiquetas guardadas: {ruta_labels}")
