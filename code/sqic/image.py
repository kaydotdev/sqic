from typing import Tuple, Optional
from PIL import Image

import numpy as np

from .quantization import sq


def image_compress(
    image: Image, colors: int, random_state: Optional[np.random.RandomState] = None
) -> Tuple[Image, np.ndarray]:
    """Returns compressed instance of original image and the reduced color palette as an instance of ndarray."""

    if random_state is None:
        random_state = np.random.RandomState()

    # Normalizing colors and extracting a color palette
    img_norm = np.array(image) / 255
    img_w, img_h, img_c = img_norm.shape
    img_colors = np.reshape(img_norm, (img_w * img_h, img_c))

    # Quantization of the color palette
    quant_colors, _ = sq(
        img_colors, n_clusters=colors, max_iter=1, random_state=random_state
    )

    # Reconstructing image by filling each pixel with neighbouring quant color
    colors_distance = np.linalg.norm(img_colors[:, np.newaxis] - quant_colors, axis=-1)
    colors_distance_idx = np.argmin(colors_distance, axis=-1)
    img_quantized = quant_colors[colors_distance_idx, :]

    # Reshaping pixels into original image dimensions
    img_restructured = np.reshape(img_quantized, (img_w, img_h, img_c))
    img_reconstructed = (img_restructured * 255).astype(np.uint8)

    return Image.fromarray(img_reconstructed), quant_colors
