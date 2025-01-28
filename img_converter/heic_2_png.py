from pathlib import Path

from PIL import Image
from pillow_heif import register_heif_opener


def heic_2_png(img_path: Path) -> Path:
    """
    Convert a HEIC image to PNG format.

    Args:
        img_path (Path): Path to the input HEIC file

    Returns:
        Path: Path object pointing to the converted PNG file
    """
    # Convert input to Path object
    output_path = img_path.with_suffix('.png')

    # Register HEIF opener with Pillow
    register_heif_opener()

    # Open and convert the image directly using PIL
    with Image.open(img_path) as image:
        # Convert colorspace if needed
        if image.mode == 'RGBA':
            image = image.convert('RGB')

        # Save as PNG
        image.save(output_path, format='PNG')

    return output_path
