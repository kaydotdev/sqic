from typing import Union, Tuple, Optional
from PIL import Image

import numpy as np

from .quantization import sq


def compress(
    image: Image,
    colors: Union[int, np.uint],
    random_state: Optional[np.random.RandomState] = None,
) -> Tuple[Image, np.ndarray, np.float64]:
    """Compresses an image by reducing its color palette using Stochastic Color Quantization.

    Parameters
    ----------
    image : Image
        The input image to be compressed as a `Pillow` Image object.
    colors : int or np.uint
         The number of colors to use in the compressed image, i.e., the size of the optimal color palette.
    random_state : np.random.RandomState, optional
        Random state for reproducibility. Defaults to None.

    Returns
    -------
    Tuple[Image, np.ndarray, np.float64]
        A tuple containing three elements:

        1. Image: A compressed version of the original image as a PIL Image object.
        2. np.ndarray: The reduced color palette as a numpy array of shape (colors, 3). Each element represents the
            intensity of each primary RGB color.
        3. np.float64: The quantization inertia from the last iteration, i.e., the minimized Wasserstein
            (or Kantorovich–Rubinstein) distance between image pixels and optimal color palette.

    Example:
    --------
    >>> from PIL import Image
    >>> import sqic
    >>> original_image = Image.open("example.jpg")
    >>> compressed_image, color_palette, inertia = sqic.compress(original_image, colors=16)
    >>> compressed_image.save("compressed_example.jpg")
    """

    if random_state is None:
        random_state = np.random.RandomState()

    # Normalizing colors and extracting a color palette
    img_norm = np.array(image) / 255
    img_w, img_h, img_c = img_norm.shape
    img_colors = np.reshape(img_norm, (img_w * img_h, img_c))

    # Quantization of the color palette
    quant_colors, quant_inertia = sq(
        img_colors, n_quants=colors, max_iter=1, random_state=random_state
    )
    quant_norm = (quant_colors * 255).astype(np.uint8)

    # Reconstructing image by filling each pixel with neighbouring quant color
    colors_distance = np.linalg.norm(img_colors[:, np.newaxis] - quant_colors, axis=-1)
    colors_distance_idx = np.argmin(colors_distance, axis=-1)
    img_quantized = quant_colors[colors_distance_idx, :]

    # Reshaping pixels into original image dimensions
    img_restructured = np.reshape(img_quantized, (img_w, img_h, img_c))
    img_reconstructed = (img_restructured * 255).astype(np.uint8)

    return Image.fromarray(img_reconstructed), quant_norm, quant_inertia
