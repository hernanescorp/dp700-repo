# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "dba0f676-0c05-4c16-8229-401e855faa24",
# META       "default_lakehouse_name": "lk_1",
# META       "default_lakehouse_workspace_id": "b609f989-9bba-4dfe-ac3f-e28288cbe234",
# META       "known_lakehouses": [
# META         {
# META           "id": "dba0f676-0c05-4c16-8229-401e855faa24"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************




import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# Load image
image = mpimg.imread("/lakehouse/default/Files/imagenes/ejemplo.png")
# Let the axes disappear
plt.axis('off')
# Plot image in the output
image_plot = plt.imshow(image)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 1. Leer imagen
imagen = Image.open("/lakehouse/default/Files/imagenes/ejemplo.png").convert("RGB")
pixeles = np.array(imagen)

# 2. Información general
print("=== ANÁLISIS DE LA IMAGEN ===")
print(f"Ancho: {imagen.width} píxeles")
print(f"Alto: {imagen.height} píxeles")
print(f"Total de píxeles: {imagen.width * imagen.height}")
print(f"Dimensiones de la matriz: {pixeles.shape}")

# 3. Identificar los colores
colores, cantidades = np.unique(
    pixeles.reshape(-1, 3),
    axis=0,
    return_counts=True
)

print("\n=== COLORES ENCONTRADOS ===")

for color, cantidad in zip(colores, cantidades):
    porcentaje = cantidad / (imagen.width * imagen.height) * 100
    print(f"RGB {color.tolist()} → {cantidad} píxeles ({porcentaje:.1f}%)")

# 4. Mostrar imagen
plt.imshow(imagen)
plt.title("Imagen original representada por números RGB")
plt.axis("off")
plt.show()


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
