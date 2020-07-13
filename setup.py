import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyVideoPreviewGenerator", # Replace with your own username
    version="1.0",
    author="@soroushamdg (soroushmpour)",
    author_email="soroushmpour@gmail.com",
    description="Python based script to generate mini previews of your videos, like tutorials or ...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/soroushamdg/pyVideoPreviewGenerator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'moviepy',
        'click'
    ],
    python_requires='>=3.6',
)