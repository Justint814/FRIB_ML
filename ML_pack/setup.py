from distutils.core import setup

setup(
name = 'FRIB_ML',
packages = ['FRIB_ML'],
version = '0.18',
license = 'MIT',
description = 'This package is used for creating training data and training a machine learning model for the FRIB level scheme project',
author = 'Justin Traywick',
author_email = 'jtraywick8@gmail.com',
url = 'https://github.com/Justint814/FRIB_ML',
download_url = 'https://github.com/Justint814/FRIB_ML/archive/refs/tags/frib14.tar.gz',
keywords = ['Machine', 'Learning', 'ML', 'train', 'data', 'level'],
install_requires = ['numpy', 'tensorflow', 'h5py', 'scikit-image'],
classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'Topic :: Software Development :: Build Tools', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.4', 'Programming Language :: Python :: 3.5', 'Programming Language :: Python :: 3.6',],
)
