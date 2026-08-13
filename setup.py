from setuptools import setup, find_packages

setup(
    name='ZetaGammaBridge',
    version='1.0.1',
    author='Manoj Punia',
    author_email='mspunia1976@gmail.com',
    description='O(1) bridge between Apery\'s constant and Euler-Mascheroni constant',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/punia-zeta/AI-Booster-ZetaGammaBridge',
    py_modules=['zeta_bridge'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: CC BY-NC-ND 4.0',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
 