from pathlib import Path
from PIL import Image

# Carpeta raíz donde están "celular" y "esp"
ROOT = Path("")

TARGET_SIZE = (128, 128)
VALID_EXTENSIONS = {".jpg", ".jpeg"}


def resize_image_in_place(image_path: Path):
    try:
        with Image.open(image_path) as img:
            img = img.convert("RGB")
            img_resized = img.resize(TARGET_SIZE, Image.LANCZOS)
            img_resized.save(image_path, format="JPEG", quality=95)

        print(f"Sobrescrita: {image_path}")

    except Exception as e:
        print(f"Error con {image_path}: {e}")


def process_folder(folder_name: str):
    folder = ROOT / folder_name

    if not folder.exists():
        print(f"No existe la carpeta: {folder}")
        return

    files = [p for p in folder.rglob("*") if p.suffix.lower() in VALID_EXTENSIONS]

    print(f"\nProcesando carpeta: {folder}")
    print(f"Imágenes encontradas: {len(files)}")

    for file_path in files:
        resize_image_in_place(file_path)


if __name__ == "__main__":
    process_folder("celular")
    process_folder("esp")
    print("\nListo. Todas las imágenes fueron reescaladas y sobrescritas.")