from setuptools import setup,find_packages
from os import path

working_directory = path.abspath(path.dirname(__file__))

with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name="offlix",  # Replace with your package name
    version="0.1.0",           # Version of your package # Your email
    long_description=long_description,  # Read the content of README.md
    long_description_content_type='text/markdown',

    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "offlix=offlix_installer.installer:main"
        ]
    },
    include_package_data=True,
    package_data={
        "offlix": ["config.json"],
    },
    install_requires=[
        # List your dependencies here
        "docker",  # For example, if you need the Docker SDK
    ],
    python_requires='>=3.6', 
    description="A tool to install and start Docker services using Docker Compose.",
    author="Suman Manna",
    author_email="manna.suman134@gmail.com",
    url="https://your-repo-url.com",
)