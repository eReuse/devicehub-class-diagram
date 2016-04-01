from setuptools import setup, find_packages

setup(
    name='DeviceHub-Class-Diagram',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/eReuse/devicehub-class-diagram',
    license='AGPLv3 License',
    author='eReuse team',
    author_email='x.bustamante@ereuse.org',
    description='A small utility to generate class diagrams from the resources of DeviceHub',
    install_requires=[
        'graphviz'
    ],
    include_package_data=True
)
