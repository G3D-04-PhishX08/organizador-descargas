import os
import shutil

# Diccionario de extensiones a carpetas
EXTENSIONES = {
    ".jpg": "Imagenes",
    ".png": "Imagenes",
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".mp3": "Musica",
    ".mp4": "Videos",
}

def main():
    carpeta_descargas = os.path.expanduser("~/Downloads")  # Carpeta de descargas del usuario
    print(f"Organizando archivos en: {carpeta_descargas}")

    for archivo in os.listdir(carpeta_descargas):
        extension = os.path.splitext(archivo)[1].lower()
        if extension in EXTENSIONES:
            carpeta_destino = os.path.join(carpeta_descargas, EXTENSIONES[extension])
            os.makedirs(carpeta_destino, exist_ok=True)
            shutil.move(
                os.path.join(carpeta_descargas, archivo),
                os.path.join(carpeta_destino, archivo)
            )
            print(f"Movido: {archivo} -> {carpeta_destino}")

if __name__ == "__main__":
    main()