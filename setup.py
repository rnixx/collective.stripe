from setuptools import setup, find_packages
import os

version = '0.3.3.dev0'

setup(name='collective.stripe',
      version=version,
      description="Stripe Credit Card Processing Integration",
      long_description=open("README.md").read(),
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='payment processing plone stripe',
      author='Jason Lantz',
      author_email='jasontlantz@gmail.com',
      url='https://github.com/collective/collective.stripe',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'stripe',
          'five.grok',
          # -*- Extra requirements: -*-
      ],
      extras_require = {
          'test': [
              'plone.app.testing',
          ]
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,

      )
