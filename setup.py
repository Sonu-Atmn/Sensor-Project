from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("#")]
    return requirements
setup(
    
    name='Fault Detection',
    version='0.0.1',
    author='Sonu Agrawal',
    author_email='sonuagrawalsun@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()   
)