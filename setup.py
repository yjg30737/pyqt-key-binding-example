from setuptools import setup, find_packages

setup(
    name='pyqt-key-binding-example',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='Example and personal practice of show and edit every key mapping data with table widget',
    url='https://github.com/yjg30737/pyqt-key-binding-example.git',
    install_requires=[
        'PyQt5'
    ]
)