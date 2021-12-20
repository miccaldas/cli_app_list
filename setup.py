from setuptools import setup

setup(
    name="cli_app_list",
    version=4.0,
    author="mclds",
    author_email="mclds@protonmail.com",
    description="Manage the famously elusive command-line app, creature.",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://codeberg.org/micaldas/cli_app_list",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["cli_app_list"],
    install_requires=[
        "mysql.connector",
        "colr",
        "questionary",
        "loguru",
        "click",
    ],
    include_package_data=True,
)
