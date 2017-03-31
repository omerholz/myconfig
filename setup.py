from setuptools import setup, find_packages
setup(
    name="myconfig",
    version="0.0.1",
    description='a config wrapper that does what I want',
    url='https://github.com/omerholz/myconfig',
    zip_safe=False,
    packages=find_packages(),

    #metadata
    author="Omer Holzinger",
    author_email="omer.holzinger@gmail.com",
    tests_require=[
        'sure==1.4.0','pytest==3.0.5'
    ]

)
