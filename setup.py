from setuptools import setup
from setuptools import find_packages

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name='expenses',
      description="This helps you to keep track of your expenses",
      packages=["expenses"],
      install_requires=requirements,
      scripts=['scripts/expenses-run'])
