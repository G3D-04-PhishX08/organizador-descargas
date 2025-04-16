import os
import shutil
import argparse

# Diccionario de extensiones -> carpetas
EXTENSIONES = {
    # Imágenes
    ".jpg": "Imagenes",
    ".jpeg": "Imagenes",
    ".png": "Imagenes",
    ".gif": "Imagenes",
    ".svg": "Imagenes",
    # Documentos
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".xlsx": "Documentos",
    ".pptx": "Documentos",
    ".txt": "Documentos",
    # Audio
    ".mp3": "Musica",
    ".wav": "Musica",
    ".flac": "Musica",
    # Video
    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    # Otros
    ".zip": "Archivos_Comprimidos",
    ".exe": "Ejecutables",
}

def organizar_archivos(ruta, dry_run=False):
    """
    Organiza los archivos en subcarpetas según su extensión.
    :param ruta: Carpeta a organizar (ej: ~/Downloads).
    :param dry_run: Si es True, solo muestra lo que haría sin mover archivos.
    """
    print(f"📂 Organizando archivos en: {ruta}")

    # Crear carpetas si no existen
    for carpeta in set(EXTENSIONES.values()):
        os.makedirs(os.path.join(ruta, carpeta), exist_ok=True)

    # Mover archivos
    for archivo in os.listdir(ruta):
        # Ignorar carpetas
        if os.path.isdir(os.path.join(ruta, archivo)):
            continue

        extension = os.path.splitext(archivo)[1].lower()
        if extension in EXTENSIONES:
            origen = os.path.join(ruta, archivo)
            destino = os.path.join(ruta, EXTENSIONES[extension], archivo)

            if dry_run:
                print(f"🚀 (Simulación) Movido: {archivo} -> {EXTENSIONES[extension]}")
            else:
                shutil.move(origen, destino)
                print(f"📦 Movido: {archivo} -> {EXTENSIONES[extension]}")

def main():
    # Configurar argumentos de línea de comandos
    parser = argparse.ArgumentParser(
        description="Organiza archivos en tu carpeta de Descargas por tipo."
    )
    parser.add_argument(
        "--ruta",
        help="Ruta a organizar (por defecto: ~/Downloads)",
        default=os.path.expanduser("~/Downloads"),
    )
    parser.add_argument(
        "--dry-run",
        help="Simula la organización sin mover archivos",
        action="store_true",
    )
    args = parser.parse_args()

    # Ejecutar
    organizar_archivos(args.ruta, args.dry_run)

if __name__ == "__main__":
    main()