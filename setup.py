"""
    GraphSense API

    GraphSense API provides programmatic access to various ledgers' addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501

    The version of the OpenAPI document: 22.10
    Contact: contact@ikna.io
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "graphsense-python"
VERSION = "22.10"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="GraphSense API",
    author="Iknaio Cryptoasset Analytics GmbH",
    author_email="contact@ikna.io",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "GraphSense API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    GraphSense API provides programmatic access to various ledgers&#39; addresses, entities, blocks, transactions and tags for automated and highly efficient forensics tasks.  # noqa: E501
    """
)
