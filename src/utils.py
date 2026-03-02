"""Input conversion utilities.

Utilities in this module stay infrastructure-focused so orchestration and model
modules remain independent from UI frameworks and transport details.
"""

from __future__ import annotations

from typing import BinaryIO

from PIL import Image, UnidentifiedImageError


class ImageLoadError(ValueError):
    """Raised when uploaded content cannot be parsed as an image."""


def load_image(uploaded_file: BinaryIO) -> Image.Image:
    """Safely convert an uploaded file-like object into a PIL image.

    Design intent:
    Centralize input conversion and normalization here so UI layers pass raw
    uploaded objects while the rest of the system works with `PIL.Image` only.
    """
    try:
        image = Image.open(uploaded_file)
        return image.convert("RGBA")
    except (UnidentifiedImageError, OSError, AttributeError) as exc:
        raise ImageLoadError("Uploaded file is not a valid image.") from exc
