import glob
import sys
from os.path import splitext, basename
from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand
import warnings

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

def _requires_from_file(filename):
    return open(filename).read().splitlines()

def get_readme():
    """ Get the README from the current directory. If there isn't one, return an empty string """
    all_readmes = sorted(glob.glob("README*"))
    if len(all_readmes) > 1:
        warnings.warn("There seems to be more than one README in this directory. Choosing the "
                      "first in lexicographic order.")
    if len(all_readmes) > 0:
        return open(all_readmes[0], 'r').read()

    warnings.warn("There doesn't seem to be a README in this directory.")
    return ""

setup(
    name="python_logging",
    version="0.1-DEV",
    url="https://github.com/tatoflam/python_logging",
    author="tatoflam",
    license="MIT",
    packages=find_packages(),
#    py_modules=[splitext(basename(path))[0] for path in glob('*.py')],
    include_package_data=True,
    zip_safe=False,
    description="Experiment for python standard logging library",
    long_description="\n" + get_readme()
)