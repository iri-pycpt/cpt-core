from pathlib import Path
from setuptools import *
import os

readme_path = Path(__file__).parent / 'README.md'
long_description = readme_path.read_text(encoding='utf-8')

setup(
    name = "cptcore",
    version = "1.0.11",
    author = "Kyle Hall",
    author_email = "kjhall@iri.columbia.edu",
    description = ("Python Interface to the International Research Institute for Climate & Society's Climate Predictability Tool "),
    license = "MIT",
    keywords = ["climate", 'predictability', 'prediction', 'precipitation', 'temperature', 'data', 'IRI'],
    url = "https://iri.columbia.edu/our-expertise/climate/tools/",
    packages=[  'cptcore', 'cptcore.functional', 'cptcore.tests' ],
    package_data={ 
        'cptcore': ['{}/src/fortran'.format(os.getenv('RECIPE_DIR')) + ''.join(['/*' for i in range(j) ]) for j in range(10) ],
        'cptcore.tests': ['{}/src/tests/data/seasonal/*'.format(os.getenv('RECIPE_DIR')), '{}/../src/tests/data/subseasonal/*'.format(os.getenv('RECIPE_DIR'))]
    },
    package_dir={ 
        '': 'src'
    },
    python_requires=">=3.0",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
    ],
)
