import logging
import re
import os
import subprocess
import sys


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

IGNORED_FILES = set()


class PylintRunner(object):

    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check_style(self, module):
        '''Runs pylint on a Python module.'''
        try:
            subprocess.check_output(['pylint', module])
            LOGGER.debug('%s PASSED.', module)
            self.passed += 1
        except subprocess.CalledProcessError as pylint_error:
            linter_message = pylint_error.output
            try:
                score = re.search(r'[-0-9]+\.\d{2}/10',
                                  linter_message).group(0)
                LOGGER.warning('%s failed PYLINT with score %s.',
                               os.path.relpath(module), score)
                self.failed += 1
            except AttributeError:
                raise


class Pep8Runner(object):

    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check_style(self, module):
        '''Runs pep8 on a Python module.'''
        try:
            subprocess.check_output(['pep8', module])
            LOGGER.debug('%s PASSED.', module)
            self.passed += 1
        except subprocess.CalledProcessError as pep8_error:
            pep8_message = pep8_error.output
            LOGGER.warning('%s FAILED PEP8', os.path.relpath(module))
            self.failed += 1
            for pep8_warning in pep8_message.splitlines():
                LOGGER.warning(pep8_warning)


def _should_check(module):
    module_name = os.path.basename(module)
    return module.endswith('.py') and module_name not in IGNORED_FILES


def _get_starting_directory(args):
    try:
        base_directory = args[1]
    except IndexError:
        base_directory = os.getcwd()
    return base_directory


def main():
    base_directory = _get_starting_directory(sys.argv)
    LOGGER.debug('Inspecting in directory %s...', base_directory)

    pylint_runner = PylintRunner()
    pep8_runner = Pep8Runner()

    for root, _, files in os.walk(base_directory):
        for name in files:
            file_path = os.path.join(root, name)
            if _should_check(file_path):
                LOGGER.info('Checking %s', file_path)
                pylint_runner.check_style(file_path)
                pep8_runner.check_style(file_path)
            else:
                LOGGER.debug('Ignore %s', file_path)

    LOGGER.info('PYLINT:\n\tPassed: %d;\n\tFailed: %d', pylint_runner.passed,
                pylint_runner.failed)

    LOGGER.info('PEP8:\n\tPassed: %d;\n\tFailed: %d', pep8_runner.passed,
                pep8_runner.failed)

    if pylint_runner.failed > 0 or pep8_runner.failed > 0:
        sys.exit()


if __name__ == '__main__':
    main()
