from distutils.core import setup

setup(
name = 'ML_package',
packages = ['ML_package-0.1'],
version = '0.1',
license = 'MIT',
description = 'This package is used for creating training data and training a machine learning model for the FRIB level scheme project',
author = 'Justin Traywick',
author_email = 'jtraywick8@gmail.com',
url = 'https://github.com/Justint814/ML_Package',
download_url = 'https://github.com/Justint814/ML_Package/archive/refs/tags/code.tar.gz',
keywords = ['Machine', 'Learning', 'ML', 'train', 'data', 'level'],
install_requires = ['numpy', 'tensorflow', 'os', 'random', 'h5py', 'math', 'shutil', 'subprocess', 'skimage'],
classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'Topic :: Software Development :: Build Tools', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.4', 'Programming Language :: Python :: 3.5', 'Programming Language :: Python :: 3.6',],
)
