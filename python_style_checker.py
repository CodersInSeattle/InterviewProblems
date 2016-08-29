import logging
import os
import re
import subprocess


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


class PythonStyleChecker(object):
    def __init__(self, linter_name):
        self.passed = 0
        self.failed = 0
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
            LOGGER.debug('%s PASSED.', module)
            self.passed += 1
        except subprocess.CalledProcessError as pylint_error:
            linter_message = pylint_error.output
            score_found = re.search(br'[-0-9]+\.\d{2}/10', linter_message)
            score = score_found.group(0)
            LOGGER.warning('%s failed PYLINT with score %s.',
                           os.path.relpath(module), score)
            self.failed += 1


class Pep8Runner(PythonStyleChecker):

    def __init__(self):
        super(Pep8Runner, self).__init__('pep8')

    def check_style(self, module):
        '''Runs pep8 on a Python module.'''
        try:
            subprocess.check_output([self.linter_name, module])
            LOGGER.debug('%s PASSED.', module)
            self.passed += 1
        except subprocess.CalledProcessError as pep8_error:
            pep8_message = pep8_error.output
            LOGGER.warning('%s FAILED PEP8', os.path.relpath(module))
            self.failed += 1
            for pep8_warning in pep8_message.splitlines():
                LOGGER.warning(pep8_warning)
