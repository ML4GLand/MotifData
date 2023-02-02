from setuptools import setup, find_packages

setup(name = 'motifdata', packages = find_packages())

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="motifdata",
    version="0.0.1",
    author="Adam Klie",
    author_email="aklie@eng.ucsd.edu",
    description="A tool for handling biological sequence motifs in Python",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/ML4GLand/MotifData",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
