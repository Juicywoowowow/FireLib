from setuptools import setup, find_packages

setup(
    name='firelib',
    version='0.1.0',
    description='Termux enhancement library for pentesting and development',
    author='Firelib Team',
    package_dir={'': 'src/python'},
    packages=find_packages(where='src/python'),
    python_requires='>=2.7',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Systems Administration',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
