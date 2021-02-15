from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='easy_ds',
  version='0.0.1',
  description='Implementation of data structures',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Jaidev chaudhary',
  author_email='jaidevchaudhary810@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Data structure', 
  packages=find_packages(),
  long_description_content_type='text/markdown',
  install_requires=[''] 
)