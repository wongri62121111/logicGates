from setuptools import setup, find_packages

setup(
    name='logic_gates',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pytest',
    ],
    author='Example Developer',
    author_email='dev@example.com',
    description='A simple logic gates implementation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
)