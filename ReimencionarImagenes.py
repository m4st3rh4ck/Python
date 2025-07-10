#!/usr/bin/env python3

"""En el laboratorio anterior, su empresa estaba actualizando su sitio web y contrató a un diseñador para que creara nuevos iconos gráficos para el sitio.
Pero el contratista entregó los diseños finales en el formato equivocado: girados 90° y demasiado grandes. ¡Uf! No pudiste ponerte en contacto con los diseñadores
y tu propio plazo de entrega se acercaba rápidamente. Tenías que usar Python para tener estas imágenes listas para el lanzamiento.

Este ejemplo es un recorrido por la actividad anterior de Qwiklab, incluyendo instrucciones detalladas y soluciones. Puedes usar este ejemplo si no pudiste completar 
el laboratorio y/o si necesitas una guía extra para completar las tareas del laboratorio.""""

import os
from PIL import Image

# Directorios
input_dir = os.path.expanduser('~/images/')
output_dir = '/opt/icons/'

# Crear directorio de salida si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Procesar cada imagen
for filename in os.listdir(input_dir):
    if not filename.startswith('.'):  # Ignorar archivos ocultos
        input_path = os.path.join(input_dir, filename)

        try:
            with Image.open(input_path) as img:
                img = img.rotate(-90).resize((128, 128)).convert("RGB")

                # Guardar con mismo nombre base pero extensión .jpeg
                name_without_ext = os.path.splitext(filename)[0]
                output_filename = name_without_ext + '.jpeg'
                output_path = os.path.join(output_dir, output_filename)

                img.save(output_path, 'JPEG')
                print(f"[✔] Guardado: {output_filename}")

        except Exception as e:
            print(f"[✘] Error con {filename}: {e}")
