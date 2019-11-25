import os
from setuptools import setup, find_packages
PACKAGES = find_packages()

opts = dict(
    name= 'AMZ_CELLPHONE_REVIEW',
    version= '0.1',
    url= 'https://github.com/cycnc35/AMZ-Cellphone-Review',
    license= 'MIT',
    author= 'KuanHsun Lu | YiCheng Chen | FengJie Chen',
    author_email= 'cycnc35@uw.edu',
    description= 'Amazon reviews analysis.',
    packages= PACKAGES,
    REQUIRES = ["numpy", "pandas", "plotly", "dash"]
)

if __name__ == '__main__':
    setup(**opts)