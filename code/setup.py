import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

if __name__ == "__main__":
    setuptools.setup(
        name="sqic",
        fullname="Stochastic Quantization for Image Compression",
        description="Lossy Image Compression with Stochastic Quantization",
        long_description=long_description,
        long_description_content_type="text/markdown",
        version="0.2.0",
        project_urls={
            "Homepage": "https://github.com/kaydotdev/sqic",
            "Issues": "https://github.com/kaydotdev/sqic/issues",
            "Repository": "https://github.com/kaydotdev/sqic.git",
        },
        author="Vladimir Norkin, Anton Kozyriev",
        author_email="a.kozyriev@kpi.ua",
        license="MIT",
        url="https://github.com/kaydotdev/sqic",
        platforms="Any",
        python_requires=">=3.8",
        include_package_data=True,
        packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
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
