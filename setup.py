from setuptools import setup, find_packages

setup(
    name="DeepSec Web",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "rich",
        "transformers"
    ],
    entry_points={
        'console_scripts': [
            'deepsec=deepsec:main'
        ]
    }
)
