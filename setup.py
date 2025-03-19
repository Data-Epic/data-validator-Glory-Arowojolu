from setuptools import setup, find_packages # type: ignore
setup(
    name= 'GloryAro_datavalidator',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    author='Glory Arowojolu',
    author_email='gloryarowojolu@gmail.com',
    description='A simple data validation package',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Data-Epic/data-validator-Glory-Arowojolu",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)