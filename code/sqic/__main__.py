import argparse
from PIL import Image
import numpy as np

import sqic


def main():
    parser = argparse.ArgumentParser(
        description="Compress an image using stochastic color quantization."
    )
    parser.add_argument("input_image_path", help="path to the input image file")
    parser.add_argument("output_image_path", help="path to save the compressed image")
    parser.add_argument(
        "colors", type=int, help="number of colors to use in the compressed image"
    )
    parser.add_argument(
        "--random_state",
        type=int,
        default=42,
        help="random state for reproducibility (default: 42)",
    )

    args = parser.parse_args()

    random_state = np.random.RandomState(args.random_state)

    img = Image.open(args.input_image_path)
    img_w, img_h = img.size

    print(
        f"> Processing image from path '{args.input_image_path}' with size {img_w}x{img_h}"
    )

    img_compressed, color_palette, inertia = sqic.compress(
        img, args.colors, random_state
    )
    img_compressed.save(args.output_image_path)

    print(f"> Saved compressed image to path '{args.output_image_path}' successfully")

    colors_hex = ["#{:02x}{:02x}{:02x}".format(r, g, b) for r, g, b in color_palette]

    print("> Color quantization inertia:", inertia)
    print("> Color palette of compressed image:", " ".join(colors_hex))


if __name__ == "__main__":
    main()
