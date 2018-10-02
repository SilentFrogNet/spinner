import setuptools

SHORT_DESCRIPTION = "A tiny library to add spinners to your code"

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

with open("VERSION", 'r') as f:
    __version__ = f.read().strip()

setuptools.setup(
    name="spinner",
    version=__version__,
    author="Ilario Dal Grande",
    author_email="ilario.dalgrande@silentfrog.net",
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/SilentFrogNet/spinner",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
)
