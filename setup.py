from setuptools import setup, find_namespace_packages

requirements = [
    "natsort",
    "pandas",
    "psutil",
    "slurmio",
    "configobj",
    "micrometa",
    "tqdm",
    "PyYAML",
    "scipy",
    "scikit-image",
    "seaborn",
]


setup(
    name="imlib",
    version="0.1.3",
    description="General data processing functions",
    install_requires=requirements,
    extras_require={
        "dev": [
            "black",
            "pytest-cov",
            "pytest",
            "coverage",
            "bump2version",
            "pre-commit",
            "flake8",
        ],
        "vedo": [
            "vedo",
        ],
    },
    python_requires=">=3.7",
    packages=find_namespace_packages(exclude=("docs", "tests*")),
    include_package_data=True,
    url="https://github.com/adamltyson/imlib",
    author="Adam Tyson",
    author_email="adam.tyson@ucl.ac.uk",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    zip_safe=False,
)
