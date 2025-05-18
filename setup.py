from setuptools import find_packages, setup
from typing import List
import requests
def get_requirements()->List[str]:
    
    requirement:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                require=line.strip()
                if require and require!='-e':
                    requirement.append(require)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement

setup(
    name="sample_one",
    version="0.0.1",
    auther="Mohsin Raza",
    author_email="mohsinraza2999@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)