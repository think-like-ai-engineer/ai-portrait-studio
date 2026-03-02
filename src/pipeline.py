"""Core orchestration pipeline for AI Portrait Studio.

The pipeline coordinates AI modules while remaining agnostic
to their internal implementations.

Design philosophy:
- UI contains no business logic
- Modules are swappable
- Pipeline owns orchestration
- Validation happens here, not inside modules
"""

from typing import Optional
from PIL import Image

from .background_removal import remove_background
from .style_transfer import apply_style


class PortraitPipeline:
    """Main orchestration class for portrait processing."""

    def __init__(self, apply_style_filter: bool = False):
        self.apply_style_filter = apply_style_filter

    def process(self, image: Image.Image) -> Image.Image:
        """Run the full portrait processing pipeline."""

        validated_image = self._validate(image)

        # Step 1: Background removal
        bg_removed = remove_background(validated_image)

        # Step 2: Optional style transformation
        if self.apply_style_filter:
            return apply_style(bg_removed)

        return bg_removed

    def _validate(self, image: Image.Image) -> Image.Image:
        """Ensure input is a valid PIL image and normalize format."""

        if not isinstance(image, Image.Image):
            raise TypeError("Input must be a PIL.Image.Image instance")

        # Normalize to RGBA for consistent downstream behavior
        return image.convert("RGBA")