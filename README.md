
# Make sure you have upgraded version of pip

Linux
```
python3 -m pip install --upgrade pip
```

## Create a project with the following structure
```
image_recognition/
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.cfg
├── src/
│   └── image_recognition_demo_test/
│       ├── __init__.py
│       └── main.py
└── tests/
```

```
touch pyproject.toml
touch setup.cfg
mkdir src
mkdir src/image_recognition_demo_test
touch src/image_recognition_demo_test/__init__.py
touch src/image_recognition_demo_test/main.py
mkdir tests
```

## pyproject.toml 

This file tells tools like pip and build how to create your project

```
[build-system]
requires = [
    "setuptools>=42",
    "wheel"
]
build-backend = "setuptools.build_meta"
```
build-system.requires gives a list of packages that are needed to build your package. Listing something here will only make it available during the build, not after it is installed.

build-system.build-backend is the name of Python object that will be used to perform the build. If you were to use a different build system, such as flit or poetry, those would go here, and the configuration details would be completely different than the setuptools configuration described below.


# Setup.cfg setup
Using setup.cfg is a best practice, but you could have a dynamic setup file using setup.py

```
[metadata]
name = example-pkg-YOUR-USERNAME-HERE
version = 0.0.1
author = Example Author
author_email = author@example.com
description = A small example package
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/pypa/sampleproject
project_urls =
    Bug Tracker = https://github.com/pypa/sampleproject/issues
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.6

[options.packages.find]
where = src

```
# Running the build
### Make sure your build tool is up to date

Linux
```
python3 -m pip install --upgrade build
```


### Create the build
```
python -m build
```

### Uploading - pre

Linux
```
python3 -m pip install --upgrade twine
```

### Upload

Linux
```
python3 -m twine upload --repository testpypi dist/*
```
