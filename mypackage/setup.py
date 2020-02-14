from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('C:\\Users\\win_n\\Python\\mypackage\\mypackage\\README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package-name>',
    author='wnyanw@gmail.com',
    author_email='wnyanw@gmailcom'
)