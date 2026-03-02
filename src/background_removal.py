"""Background removal module boundary.

This module encapsulates portrait segmentation behind a stable function
contract so model internals can evolve without changing pipeline orchestration.
"""

from io import BytesIO
from PIL import Image
from rembg import remove


def remove_background(image: Image.Image) -> Image.Image:
    """Remove the image background using `rembg`.

    This function is intentionally pure:
    - No I/O
    - No validation
    - No side effects
    - Returns a new RGBA PIL Image

    The pipeline owns validation and orchestration.
    """

    output = remove(image.convert("RGBA"))

    # rembg may return raw bytes depending on configuration
    if isinstance(output, bytes):
        output = Image.open(BytesIO(output))

    return output.convert("RGBA")