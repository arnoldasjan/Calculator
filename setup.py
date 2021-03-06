from setuptools import setup

VERSION = '1.0.0'
DESCRIPTION = 'TC 2.1.3 Calculator Package'
LONG_DESCRIPTION = 'TC 2.1.3 Calculator Package with add and multiply functions'

setup(
    name="calculator",
    version=VERSION,
    author="Arnoldas Januska",
    author_email="<januska.arnoldas@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    py_modules=["actions", "list_actions"],
    package_dir={'', 'calculator'},
    keywords=['python', 'calculator package'],
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
    ]
)
