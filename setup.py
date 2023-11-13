from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='example_pkg',
    version='0.1.0',
    author='Your Name',
    author_email='your@email.com',
    description='A simple example package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/example_pkg',
    packages=find_packages(),
    install_requires=[
        'requests',  # example dependency
        'numpy',     # example dependency
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
