from setuptools import setup

AUTHOR_USER_NAME="nagen01"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = []
setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    package=[SRC_REPO],
    python_requires=">=3.6"
)