from setuptools import setup

setup(
   name='quadruped_kinematics',
   version='1.0',
   description='A useful module',
   author='Mike Romanko',
   author_email='foomail@foo.com',
   packages=['quadruped_kinematics'],  #same as name
   install_requires=['numpy'], #external packages as dependencies
)
