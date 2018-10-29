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
    keywords='spinner spinners thread progressbar progress bar loading loading-spinner',
    url="https://github.com/SilentFrogNet/spinner",
    license='GPLv3',
    project_urls={
        'Documentation': 'https://github.com/SilentFrogNet/spinner/wiki',
        'Source': 'https://github.com/SilentFrogNet/spinner',
    },
    packages=setuptools.find_packages(),
    python_requires='>=3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
)
