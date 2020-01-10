#!/usr/bin/env python
"""
Build script for yum-presto.
"""
from setuptools import setup, find_packages

setup (name = "yum-presto",
    version = '0.4.4',
    packages = find_packages(), 
    description = "Utilizes the work done on deltarpm to provide faster, smaller size downloads to Fedora users.",
    author = 'Jonathan Dieter',
    author_email = 'jdieter@lesbg.com',
    license = 'GPLv2+',
    platforms=["Linux"],

    data_files=[('/usr/lib/yum-plugins/', ['presto.py']),
                ('/etc/yum/pluginconf.d/', ['presto.conf'])],

    classifiers=['License :: OSI Approved ::  GNU General Public License (GPL)',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 ],
)
