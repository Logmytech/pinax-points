import codecs

from os import path
from setuptools import find_packages, setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="a points, positions and levels app for Django",
    name="pinax-points",
    long_description=read("README.rst"),
    version="0.4",
    url="http://pinax-points.rtfd.org/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "points": [
            "templates/pinax/points/*.html",
            "templates/admin/pinax/points/awardedpointvalue/*.html",
        ]
    },
    install_requires=[
        "Django>=1.8"
    ],
    test_suite="runtests.runtests",
    tests_require=[
    ],
    extras_require={
        "pytest": ["pytest", "pytest-django"]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
