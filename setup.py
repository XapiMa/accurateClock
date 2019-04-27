import setuptools
 
setuptools.setup(
    name="accurateClock",
    version="1.0",
    author="Naoki Harima",
    author_email="hurry4170@gmail.com",
    description="accurateClock provide accurate time",
    long_description="The accurateClock provide accurate time than the computer's internal clock. This tool calculates the built-in clock delay based on the NTP information provided by NICT and provides more accurate UNIX time.",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6.0",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)