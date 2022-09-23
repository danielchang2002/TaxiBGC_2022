import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TaxiBGC-package",
    version="1.0.0",
    author="Daniel Chang",
    author_email="danielchang2002@gmail.com",
    description="TaxiBGC (Taxonomy-guided Identification of Biosynthetic Gene Clusters)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points={"console_scripts": ["taxibgc=TaxiBGC.__main__:main"]},
    package_data={"TaxiBGC": ["TaxiBGC_databases/*"]},
)
