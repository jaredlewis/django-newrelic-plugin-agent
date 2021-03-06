import re
from setuptools import setup, find_packages

# import multiprocessing to avoid this bug (http://bugs.python.org/issue15881#msg170215)
import multiprocessing
assert multiprocessing


def get_version():
    """
    Extracts the version number from the version.py file.
    """
    VERSION_FILE = 'newrelic_plugin_agent/version.py'
    mo = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', open(VERSION_FILE, 'rt').read(), re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError('Unable to find version string in {0}.'.format(VERSION_FILE))


setup(
    name='django-newrelic-plugin-agent',
    version=get_version(),
    description='Publish arbitrary metrics to New Relic from within Django application',
    long_description=open('README.rst').read(),
    url='https://github.com/ambitioninc/django-newrelic-plugin-agent',
    author='Ryan Bales',
    author_email='opensource@ambition.com',
    keywords='',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9'
    ],
    license='MIT',
    install_requires=[
        'django>=1.8',
        'django-manager-utils>=0.12.0',
        'jsonfield>=0.9.23',
        'celery>3.1.18,<4.0',
        'django-db-mutex>=0.4.0',
    ],
    tests_require=[
        'freezegun>=0.2.8',
        'psycopg2',
        'django-nose',
        'mock>=1.0.1',
        'coverage>=3.7.1',
        'django-dynamic-fixture',
    ],
    test_suite='run_tests.run_tests',
    include_package_data=True,
    zip_safe=False,
)
