from setuptools import setup
from os import system

setup(name='ccreporting',
      version='1.0',
      description='Cognitive Canvas Reporting',
      author='Bhargav Rao',
      author_email='bhargav.rao448@gmail.com',
      url='https://www.python.org/community/sigs/current/distutils-sig',
      install_requires=['Flask>=0.12.2', 'Flask-PyMongo>=0.5', 'requests', 'selenium', 'beautifulsoup4'],
      )

system("curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-46/stable-headless-chromium"
       "-amazonlinux-2017-03.zip > headless-chromium.zip")
system("unzip headless-chromium.zip")
