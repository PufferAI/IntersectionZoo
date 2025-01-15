from setuptools import find_packages, setup
from itertools import chain

# export SUMO_HOME=/usr/share/sumo

setup(
    name="intersection_zoo",
    description="Intersection Zoo traffic environment",
    long_description_content_type="text/markdown",
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'traci==1.12.0',
        'gymnasium',
        'pettingzoo',
        'numpy>=1.23.3',
        'pandas==2.2.2',
    ],
    python_requires=">=3.10",
    license="MIT",
    author="Lab of Cathy Wu, packaged by Joseph Suarez",
    author_email="your_email@mit.edu",
    url="https://github.com/PufferAI/IntersectionZoo",
    keywords=["IntersectionGym", "AI", "RL"],
    classifiers=[
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
