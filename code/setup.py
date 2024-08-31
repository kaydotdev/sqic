import setuptools


if __name__ == "__main__":
    setuptools.setup(
        name="sqic",
        fullname="Stochastic Quantization for Image Compression",
        description="Lossy Image Compression with Stochastic Quantization",
        long_description="",
        version="0.1.0",
        author="Vladimir Norkin, Anton Kozyriev",
        author_email="a.kozyriev@kpi.ua",
        license="MIT",
        url="https://github.com/kaydotdev/sqic",
        platforms="Any",
        python_requires=">=3.11",
        packages=setuptools.find_packages(exclude=["tests"]),
        scripts=[],
        classifiers=[
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: 3.13",
            "Programming Language :: Python :: 3.14",
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
