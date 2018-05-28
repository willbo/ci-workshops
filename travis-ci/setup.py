from setuptools import setup
setup(name='TravisCIWorkshop',
      version='0.1.0',
      description='A workshop for Travis',
      url='https://github.com/caffalaughrey/ci-workshops',
      author='Aaron Caffrey',
      author_email='acaffrey@salesforce.com',
      license='MIT',
      packages=['TravisCIWorkshop'],
      package_dir = {'TravisCIWorkshop': 'src'},
      zip_safe=False,
      install_requires=[
          'pytest',
          'pytest-runner',
          'responses'],
      tests_require=['pytest']
      )
