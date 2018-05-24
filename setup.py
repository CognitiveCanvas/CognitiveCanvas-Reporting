from setuptools import setup

setup(name='ccreporting',
      version='1.0',
      description='Cognitive Canvas Reporting',
      author='Bhargav Rao',
      author_email='bhargav.rao448@gmail.com',
      url='https://www.python.org/community/sigs/current/distutils-sig',
      install_requires=['Flask>=0.12.2', 'Flask-PyMongo>=0.5', 'requests', 'selenium', 'beautifulsoup4'],
      )