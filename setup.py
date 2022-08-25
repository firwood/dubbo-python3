# -*- coding: utf-8 -*-
"""
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
"""

from setuptools import setup, find_packages

setup(
    name='python-dubbo3',
    version='0.0.1',
    url='',
    author='',
    author_email='',
    description='Python3 Dubbo Client. Code base base https://github.com/apache/dubbo-python2 . Use Dubbo v2.6.2,v2.7.3',
    license='Apache License 2.0',
    packages=find_packages(exclude=['tests', 'tools']),
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: Chinese (Simplified)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'kazoo==2.8.0'
    ],
)
