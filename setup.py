import os
from setuptools import setup


README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-trumbowyg',
    version='2.0.1',
    packages=['trumbowyg'],
    include_package_data=True,
    install_requires=[],
    author='sandino',
    author_email='vdjangofan@gmail.com',
    url='https://github.com/sandino/django-trumbowyg',
    license='The MIT License (MIT)',
    description='Trumbowyg (WYSIWYG editor) integration app for Django admin.',
    long_description=README,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
