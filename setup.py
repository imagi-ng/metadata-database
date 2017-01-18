import setuptools

setuptools.setup(
    author="Allen Goodman",
    author_email="allen.goodman@icloud.com",
    extras_require={
        "test": [
            "coverage",
            "pytest"
        ]
    },
    install_requires=[
        "alembic",
        "cymysql",
        "flask",
        "flask_sqlalchemy"
    ],
    license="MIT",
    name="metadata_database",
    package_data={
        "metadata_database": [
            "data/annotations.csv",
            "data/annotators.csv",
            "data/categories.csv",
            "data/channels.csv",
            "data/experiments.csv",
            "data/imageable.csv",
            "data/images.csv",
            "data/plates.csv",
            "data/stainable.csv",
            "data/stains.csv"
            "data/wells.csv"
        ]
    },
    packages=setuptools.find_packages(
        exclude=[
            "tests"
        ]
    ),
    url="https://github.com/imagi-ng/metadata_database-database",
    version="0.1.0"
)
