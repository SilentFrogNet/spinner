import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spinner",
    version="0.1",
    author="Ilario Dal Grande",
    author_email="ilario.dalgrande@silentfrog.net",
    description="A tiny library to add spinners to your code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SilentFrogNet/spinner",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
