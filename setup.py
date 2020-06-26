import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="capture_demonstration-rezaahmadzadeh", 
    version="0.0.1",
    author="Reza Ahmadzadeh",
    author_email="reza@cs.uml.edu",
    description="A package for capturing demonstrations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rezaahmadzadeh/capture_demonstration",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
