import setuptools


if __name__ == "__main__":
    setuptools.setup(
        name="sqic",
        fullname="Stochastic Quantization for Image Compression",
        description="Lossy Image Compression with Stochastic Quantization",
        long_description="Lossy image compression algorithms play a crucial role in various domains, including network "
        "data transfer, data storage, graphics, and image processing. As image information density "
        "increases, so do the resources required for processing and transmission. One of the most "
        "prominent approaches to address this challenge is color quantization, proposed by Orchard "
        "et al. (1991). This technique optimally maps each pixel of an image to a color from a "
        "limited palette, maintaining image resolution while significantly reducing information "
        "content. Color quantization can be interpreted as a clustering problem (Krishna et al. "
        "(1997), Wan (2019)), where image pixels are represented in a three-dimensional space, with "
        "each axis corresponding to the intensity of an RGB channel. However, Norkin et al. (2024) "
        "demonstrated that scaling traditional algorithms like K-means can be challenging for large "
        "data, such as modern images with millions of colors. This paper reframes color quantization "
        "as a three-dimensional stochastic transportation problem between the set of image pixels and "
        "an optimal color palette, where the number of colors is a predefined hyperparameter. We "
        "employ Stochastic Quantization (SQ) with a seeding technique proposed by Arthur et al. "
        "(2007) to enhance the scalability of color quantization. This method introduces a "
        "probabilistic element to the quantization process, potentially improving efficiency and "
        "adaptability to diverse image characteristics. To demonstrate the efficiency of our "
        "approach, we present experimental results using images from the ImageNet dataset. These "
        "experiments illustrate the performance of our SQ-based method in terms of compression "
        "quality, computational efficiency, and scalability compared to traditional color "
        "quantization techniques.",
        version="0.1.0",
        author="Vladimir Norkin, Anton Kozyriev",
        author_email="a.kozyriev@kpi.ua",
        license="MIT",
        url="https://github.com/kaydotdev/sqic",
        platforms="Any",
        python_requires=">=3.8",
        packages=setuptools.find_packages(exclude=["tests"]),
        scripts=[],
        classifiers=[
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Topic :: Multimedia :: Graphics :: Editors :: Raster-Based",
        ],
        keywords=[
            "non-convex optimization",
            "stochastic quantization",
            "color quantization",
            "lossy compression",
        ],
        install_requires=["numpy>=1.26.4,<2", "pillow>=10.4.0,<2"],
    )
