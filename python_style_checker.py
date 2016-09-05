import os
import re
import subprocess


class PythonStyleChecker(object):
    def __init__(self, linter_name):
        self.passed = 0
        self.failed = set()
        self._linter_name = linter_name

    @property
    def linter_name(self):
        return self._linter_name

    def check_style(self, module):
        raise NotImplementedError


class PylintRunner(PythonStyleChecker):

    def __init__(self):
        super(PylintRunner, self).__init__('pylint')

    def check_style(self, module):
        '''Runs pylint on a Python module.'''
        try:
            subprocess.check_output([self.linter_name, module])
            self.passed += 1
        except subprocess.CalledProcessError as pylint_error:
            self.failed.add(os.path.relpath(module))


class Pep8Runner(PythonStyleChecker):

    def __init__(self):
        super(Pep8Runner, self).__init__('pep8')

    def check_style(self, module):
        '''Runs pep8 on a Python module.'''
        try:
            subprocess.check_output([self.linter_name, module])
            self.passed += 1
        except subprocess.CalledProcessError as pep8_error:
            self.failed.add(os.path.relpath(module))
