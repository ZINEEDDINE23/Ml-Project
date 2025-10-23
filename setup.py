from setuptools import setup,find_packages
from typing import List

Hidden_E_Dot='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        
        requirements=file_obj.readlines()
        requirements=[req.strip() for req in requirements]
        
        if Hidden_E_Dot in requirements:
            requirements.remove(Hidden_E_Dot)
        
    return requirements

setup(
    name='Ml project',
    author='Zine Eddine Tahri',
    version='0.1.0',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
    
)