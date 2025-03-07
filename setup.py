from setuptools import setup, find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path: str) -> List[str]:

    'this file will return the list of requirements from the file'
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirments]
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.1',  # Update the version number for new releases
    description='A short description of the project.',
    author='Faizan Arshad',
    author_email='faizanarshad124@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

