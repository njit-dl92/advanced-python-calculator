from setuptools import setup, find_packages

setup(
    name='advanced-python-calculator',
    version='1.0',
    packages=find_packages(),  # Automatically finds all packages in your project
    install_requires=[
        'pandas',
        # Add more dependencies if needed
    ],
)
