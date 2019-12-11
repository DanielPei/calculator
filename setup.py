# !/bin/python
# -*- coding:utf-8 -*-

# @Author  : Daniel.Pei
# @Email   : peixq1222@icloud.com
# @Created : 2019/12/11 23:21

from setuptools import setup, find_packages

ProjectName = 'calculator_demo'
Author = 'DanielPei'
Email = 'peixq1222@icloud.com'
URL = 'https://github.com/DanielPei/calculator.git'
DocUrl = 'https://sphinx-autodoc-example.readthedocs.io/en/latest/'

setup(
    name=ProjectName,
    url=URL,
    author=Author,
    author_email=Email,
    maintainer=Author,
    maintainer_email=Email,
    version='0.0.1',
    description='Python Calculator',
    keywords='calculator',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    python_requires='>=3.7',
    project_urls={
        'Documentation': DocUrl,
        'Source': URL,
        'Tracker': '%s/issues' % URL,
    },
    # install_requires=open('requirements.txt').read().splitlines(),

)
