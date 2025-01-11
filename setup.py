from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

AUTHOR_NAME = 'MAHRUKH MALIK'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit','numpy','plotly','pandas','scikit-learn','matplotlib']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='mahrukh711@gmail.com',
    description='A simple python package for Coffee recommendation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[SRC_REPO],  # Corrected from 'package' to 'packages'
    python_requires='>=3.7',
    install_requires=LIST_OF_REQUIREMENTS,
)
