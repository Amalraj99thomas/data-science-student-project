from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    returns list of requirements as a list of strings
    excluding -e
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

#Project details
setup(
name='studperform',
version='0.0.1',
author='Amal',
author_email='reachthomas98@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)