"""Style transformation module boundary.

This module is intentionally narrow: it owns style application only. The current
implementation is a lightweight placeholder so the pipeline can evolve without
coupling to a specific generative or artistic model.
"""

from PIL import Image, ImageFilter


def apply_style(image: Image.Image) -> Image.Image:
    """Apply a simple placeholder style effect.

    Design intent:
    Keep a stable function contract that can later point to more advanced style
    transfer models without requiring pipeline interface changes.
    """
    return image.filter(ImageFilter.SMOOTH)
