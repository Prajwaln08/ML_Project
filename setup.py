from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT= "-e ."
def get_requirements(file_path:str)-> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path, mode='r') as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.removd(HYPEN_E_DOT)
    
    return requirements

setup(
name = 'mlproject1',
version = '1.0',
author='Prajwal',
author_email='nerkarprajwal08@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)